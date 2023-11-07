import pathlib
import pycountry


def unicode_flag(country_code):
    off = ord('🇦') - ord('A')
    return chr(ord(country_code[0]) + off) + chr(ord(country_code[1]) + off)


src_dir = pathlib.Path(globals()["src_dir"])

src_files = list((src_dir / "assets").glob("*"))
src_files = [f for f in src_files if "photo_" in f.name]
src_files.sort(reverse=True)

output = "Title: Photos\n"
output += "raw: true\n"
output += "Description: A collection of photos I've taken in various countries.\n"
output += "Icon: logo.jpg\n"
output += "Pos: 02_00\n\n"
output += "<h1>Photos</h1>\n\n"
output += "<p>A collection of photos I've taken in various countries.</p>\n\n"

for src_file in src_files:
    photo_info = src_file.name.split(".")[0]
    date = "/".join(photo_info.split("_")[1].split("-")[:3])
    country_code = photo_info.split("_")[2].upper()

    country_name = pycountry.countries.get(alpha_2=country_code).name

    output += f"""
        <div class="thumbnail">
            <img alt="image from {date}" src="thumbnails/{src_file.name}"><a href="expanded_images/{src_file.name}.html">click to expand</a>
        </div>\n
    """

    output += f"{unicode_flag(country_code)} {country_name}, {date}\n<br><br>\n"
