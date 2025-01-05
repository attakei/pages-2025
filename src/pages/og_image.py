"""Image generator for opengraph."""

import base64
from pathlib import Path

import click
from cairosvg import svg2png  # type: ignore
from jinja2 import Template


TEMPLATES = {
    "default": """
<svg width="1200" height="630" xmlns="http://www.w3.org/2000/svg">
  <rect width="1200" height="630" fill="green" />
  <rect width="90%" height="90%" x="5%" y="5%" rx="10" ry="10" fill="white" />
  <image width="320" height="320" x="100" y="150" href="data:{{ logo.type }};base64,{{ logo.base64 }}" />
  <text x="440" y="315" font-size="96">{{ site.name }}</text>
</svg>
    """.strip(),
}

here = Path(__file__).parent
root = here.parents[1]

logo = {
    "path": root / "contents" / "_static" / "images" / "icon-attakei@2x.png",
    "type": "image/png",
}


@click.command()
@click.option(
    "--template",
    type=str,
    default="default",
)
@click.option("--format", type=str, default="svg")
@click.option("--text", type=str, default="")
@click.argument(
    "output",
    type=click.Path(
        file_okay=True,
        dir_okay=False,
        readable=True,
        writable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
def main(template: str, format: str, text: str, output: Path):
    """Generate ogp image from template."""
    tmpl = Template(TEMPLATES[template])
    logo["base64"] = base64.b64encode(logo["path"].read_bytes()).decode()  # type: ignore[attr-defined]
    ctx = {
        "logo": logo,
        "site": {
            "name": "attakei pages",
        },
        "text": text,
    }
    svg = tmpl.render(ctx)
    match format:
        case "svg":
            output.write_text(svg)
        case "png":
            svg2png(bytestring=svg, write_to=str(output))
        case _:
            print(f"Unsupported format '{format}'")
            pass
