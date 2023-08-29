import pathlib
import markdown

# so the linter doesn't complain about undefined variables
src_dir = locals()["src_dir"]

src_dir = pathlib.Path(src_dir)

src_files = list((src_dir / "pages").glob("*"))
src_files.sort()

output = "raw: true\n"

for src_file in src_files:
    md = markdown.Markdown(extensions = ["meta"])
    md.convert(src_file.read_text())

    indent = len(src_file.name.split("_")) - 1
    title = md.Meta.get('title', [''])[0]

    output += f"<div id=\"nav-item\">{'&nbsp;' * indent * 2}{title}</div>"