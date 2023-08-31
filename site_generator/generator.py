import pathlib
import shutil
import sys
import markdown
import tidylib
import re
from PIL import Image, ImageOps

def get_src_dir():
    return (pathlib.Path() / sys.argv[1]).absolute()

def get_out_dir():
    return (pathlib.Path() / sys.argv[2]).absolute()

def parse_file(in_file: pathlib.Path) -> (str, dict):
    file_type = in_file.suffix
    file_contents_raw = in_file.read_text()

    if file_type == ".py":
        global_vars = {"src_dir": str(get_src_dir()), "parse_file": parse_file}
        local_vars = {}
        exec(file_contents_raw, global_vars, local_vars)
        file_contents_raw = local_vars.get("output", "")
    
    file_contents = re.sub(
        r'!\[([^\]]*)\]\(assets/(\S*)\)',
        r'<div class="thumbnail"><img alt="\1" src="thumbnails/\2"><a href="assets/\2">click to expand image</a></div>',
        file_contents_raw
    )

    md = markdown.Markdown(extensions = ["extra", "meta", "codehilite"])
    file_contents = md.convert(file_contents)
    metadata = md.Meta

    # print(file_contents)

    if metadata.get("raw", ["false"])[0] == "true":
        file_contents = re.match(r'^(.*:.*\n)*([\s\S]*)$', file_contents_raw).groups()[1].strip()
    
    return file_contents, metadata

def make_page(in_file: pathlib.Path, header: str, footer: str, nav: str) -> str:
    content, metadata = parse_file(in_file)

    html_file = "<!doctype html>"
    html_file += "<html>"
    html_file += "<head>"
    html_file += f"<title>Kai | {metadata.get('title', [''])[0]}</title>"
    html_file += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>"
    html_file += "<link rel=\"stylesheet\" href=\"styles/main.css\"/>"
    html_file += "<link rel=\"stylesheet\" href=\"styles/highlight.css\"/>"
    html_file += f"<link rel=\"icon\" href=\"assets/{metadata.get('icon', [''])[0]}\"/>"
    html_file += "</head>"
    html_file += "<body>"
    html_file += f"<div class=\"header\">{header}</div>"
    html_file += "<div class=\"body\">"
    html_file += f"<div class=\"nav\">{nav}</div>"
    html_file += f"<div class=\"content\">{content}</div>"
    html_file += "</div>"
    html_file += f"<div class=\"footer\">{footer}</div>"
    html_file += "</body>"

    # make external links (any link with https://) open in another tab
    html_file = re.sub(r'<a([^>]*href="https?:\/\/[^"]*")>', r'<a \1 target="_blank">', html_file)

    # replace .md and .py with .html if not external link
    html_file = re.sub(r'href="((?!https?:\/\/)[^"]*)(?:(?:.md)|(?:.py))"', r'href=\1.html', html_file)

    return tidylib.tidy_document(html_file)[0]

if len(sys.argv) != 3:
    print("ERROR: usage: generator.py [source dir] [out dir]")
    exit()

src_dir = get_src_dir()
out_dir = get_out_dir()

print(f"src_dir: {src_dir}")
print(f"out_dir: {out_dir}")

if out_dir.exists():
    shutil.rmtree(out_dir)

out_dir.mkdir()
(out_dir / "assets").mkdir()
(out_dir / "thumbnails").mkdir()
(out_dir / "styles").mkdir()


# copy assets
src_files = list((src_dir / "assets").glob("*"))

for i, src_file in enumerate(src_files):
    print(f"[asset {i + 1}/{len(src_files)}]: {src_file}")

    out_file_orig = out_dir / "assets" / src_file.name
    out_file_thumb = out_dir / "thumbnails" / src_file.name

    try:
        image = ImageOps.exif_transpose(Image.open(src_file))
        if image.size[0] > 640 or image.size[1] > 480:
            scale = min(640 / image.size[0], 480 / image.size[1])
            image.resize((int(image.size[0] * scale), int(image.size[1] * scale)))
        image.save(out_file_thumb, quality=60)
    except:
        out_file_thumb.touch()
        out_file_thumb.write_bytes(src_file.read_bytes())

    out_file_orig.touch()
    out_file_orig.write_bytes(src_file.read_bytes())


# copy styles
src_files = list((src_dir / "styles").glob("*"))

for i, src_file in enumerate(src_files):
    print(f"[style {i + 1}/{len(src_files)}]: {src_file}")

    out_file = out_dir / "styles" / src_file.name
    out_file.touch()
    out_file.write_text(src_file.read_text())

header = parse_file(next((src_dir / "shared").glob("header.*")))[0]
footer = parse_file(next((src_dir / "shared").glob("footer.*")))[0]
nav = parse_file(next((src_dir / "shared").glob("nav.*")))[0]

# convert and copy pages
src_files = list((src_dir / "pages").glob("*"))

for i, src_file in enumerate(src_files):
    print(f"[page {i + 1}/{len(src_files)}]: {src_file}")

    out_file = (out_dir / src_file.name).with_suffix(".html")
    out_file_contents = make_page(src_file, header, footer, nav)
    out_file.touch()
    out_file.write_text(out_file_contents)

