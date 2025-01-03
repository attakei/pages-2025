# flake8: noqa


class Router:
    """starlette.routing.Router から必要最低限のとこだけ抜粋"""

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        # 前略

        if scope["type"] == "http" and self.redirect_slashes and scope["path"] != "/":
            # リクエストパスが / で終わらない時に、リダイレクト可能性があるので / 付きのデータを用意
            redirect_scope = dict(scope)
            if scope["path"].endswith("/"):
                redirect_scope["path"] = redirect_scope["path"].rstrip("/")
            else:
                redirect_scope["path"] = redirect_scope["path"] + "/"

            # ルーティング情報からリダイレクト先とマッチする情報があるか探し、
            # 見つかったら、リダイレクトレスポンスを返してしまうs
            for route in self.routes:
                match, child_scope = route.matches(redirect_scope)
                if match != Match.NONE:
                    redirect_url = URL(
                        scope=redirect_scope
                    )  # <= この中身がhostしかみない
                    response = RedirectResponse(url=str(redirect_url))
                    await response(scope, receive, send)
                    return
        # 後略
