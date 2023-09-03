import pathlib

src_dir = pathlib.Path(globals()["src_dir"])

src_files = list((src_dir / "assets").glob("*"))
src_files = [f for f in src_files if "photos_" in f.name]
src_files.sort(reverse=True)

output = "Title: Photos\n"
output += "Description: A collection of photos I've taken in various countries.\n"
output += "Icon: logo.jpg\n"
output += "Pos: 02_00\n\n"
output += "# Photos\n\n"
output += "A collection of photos I've taken in various countries.\n\n"

for src_file in src_files:
    title = "/".join(src_file.name.split("_")[1].split("-")[:3])

    output += f"## {title}\n\n"
    output += f"![image from {title}](assets/{src_file.name})\n\n"