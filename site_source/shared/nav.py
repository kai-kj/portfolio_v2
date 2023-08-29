import pathlib
import markdown

# so the linter doesn't complain about undefined variables
src_dir = locals()["src_dir"]

src_dir = pathlib.Path(src_dir)

index_file = list((src_dir / "pages").glob("index*"))[0]

src_files = list((src_dir / "pages").glob("*"))
src_files.sort()

# make sure index is top page
src_files.remove(index_file)
src_files.insert(0, index_file)

output = "raw: true\n"
output += "<div class=\"title\">Pages</div>"
output += "<hr>"

for src_file in src_files:
    md = markdown.Markdown(extensions = ["meta"])
    md.convert(src_file.read_text())

    indent = len(src_file.name.split("_")) - 1
    title = md.Meta.get('title', [''])[0]

    output += f"<div class=\"item\">{'&nbsp;' * indent * 2}<a href=\"{src_file.name}\">{title}</a></div>"