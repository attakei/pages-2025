from typing import List, Tuple

from starlette.types import ASGIApp, Receive, Scope, Send

Headers = List[Tuple[bytes, bytes]]


class ForwardedHostMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return
        scope["headers"] = self.remap_headers(
            scope["headers"], b"host", b"x-forwarded-host"
        )
        await self.app(scope, receive, send)
        return

    def remap_headers(self, src: Headers, before: bytes, after: bytes) -> Headers:
        """元のヘッダーリストから、
        - 無関係なものはそのままコピーして
        - 置換対象は一旦退避して
        - 結果に応じて再追記する
        """
        remapped = []
        before_value = None
        after_value = None
        for header in src:
            k, v = header
            if k == before:
                before_value = v
                continue
            elif k == after:
                after_value = v
                continue
            remapped.append(header)
        if after_value:
            remapped.append((before, after_value))
        elif before_value:
            remapped.append((before, before_value))
        return remapped
