import pathlib

src_dir = pathlib.Path(globals()["src_dir"])

index_file = list((src_dir / "pages").glob("index*"))[0]

src_files = list((src_dir / "pages").glob("*"))
src_files = [(f, (globals()["parse_file"])(f)[1]) for f in src_files]
src_files.sort(key=lambda f: f[1].get('pos', [''])[0])

output = "raw: true\n"

for f in src_files:
    if f[1].get("pos", [""])[0] == "":
        continue

    indent = len(f[0].name.split("_")) - 1
    title = f[1].get('title', [''])[0]
    output += f"<div class=\"item\">{'&nbsp;' * indent * 2}<a href=\"{f[0].name}\">{title}</a></div>"

    if f[0].name == "photos.py":
        photo_files = list((src_dir / "assets").glob("*"))
        photo_files = [p.name for p in photo_files if "photo_" in p.name]
        photo_files.sort(reverse=True)

        current_year = None
        for p in photo_files:
            year = p.split("_")[1].split("-")[0]
            print(year, current_year)
            if year != current_year:
                current_year = year
                output += f"<div class=\"item\">{'&nbsp;' * (indent + 1) * 2}<a href=\"{f[0].name}#{year}\">{year}</a></div>"
