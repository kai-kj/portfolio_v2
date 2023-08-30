import pathlib

src_dir = pathlib.Path(locals()["src_dir"])

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
    metadata = locals()["parse_file"](src_file)[1]

    indent = len(src_file.name.split("_")) - 1
    title = metadata.get('title', [''])[0]
    
    output += f"<div class=\"item\">{'&nbsp;' * indent * 2}<a href=\"{src_file.name}\">{title}</a></div>"