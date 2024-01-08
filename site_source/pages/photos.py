import pathlib


def unicode_flag(country_code):
    off = ord('🇦') - ord('A')
    return chr(ord(country_code[0]) + off) + chr(ord(country_code[1]) + off)


src_dir = pathlib.Path(globals()["src_dir"])

src_files = list((src_dir / "assets").glob("*"))
src_files = [f for f in src_files if "photo_" in f.name]
src_files.sort(reverse=True)

output = "Title: Photos\n"
output += "Description: A collection of photos I've taken in various countries.\n"
output += "Icon: logo.jpg\n"
output += "Pos: 02_00\n\n"
output += "# Photos\n\n"
output += "A collection of photos I've taken in various countries.\n\n"

for src_file in src_files:
    photo_info = src_file.name.split(".")[0]
    date = "/".join(photo_info.split("_")[1].split("-")[:3])
    country_code = photo_info.split("_")[2].upper()

    output += f"<br><div align=\"center\">{unicode_flag(country_code)}&ensp;{date}</div>\n"
    output += f"![photo from {date}](assets/{src_file.name})\n"
