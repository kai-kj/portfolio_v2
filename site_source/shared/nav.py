import pathlib

src_dir = pathlib.Path(globals()["src_dir"])

index_file = list((src_dir / "pages").glob("index*"))[0]

src_files = list((src_dir / "pages").glob("*"))
src_files = [(f, (globals()["parse_file"])(f)[1]) for f in src_files]
src_files.sort(key=lambda f: f[1].get('pos', [''])[0])

output = "raw: true\n"
output += "<div class=\"title\">Pages</div>"
output += "<hr>"

for f in src_files:
    if f[1].get("pos", [""])[0] == "": continue

    indent = len(f[0].name.split("_")) - 1
    title = f[1].get('title', [''])[0]
    output += f"<div class=\"item\">{'&nbsp;' * indent * 2}<a href=\"{f[0].name}\">{title}</a></div>"