import pathlib
import shutil
import sys
import markdown
import tidylib
import re

def get_src_dir():
    return (pathlib.Path() / sys.argv[1]).absolute()

def get_out_dir():
    return (pathlib.Path() / sys.argv[2]).absolute()

def parse_file(in_file: pathlib.Path) -> (str, dict):
    file_type = in_file.suffix
    file_contents_raw = in_file.read_text()

    if file_type == ".py":
        local_vars = {"src_dir": str(get_src_dir())}
        exec(file_contents_raw, {}, local_vars)
        file_contents_raw = local_vars.get("output", "")
    
    md = markdown.Markdown(extensions = ["meta"])
    file_contents = md.convert(file_contents_raw)
    metadata = md.Meta

    if metadata.get("raw", ["false"])[0] == "true":
        file_contents = re.match(r"^(.*:.*\n)*([\s\S]*)$", file_contents_raw).groups()[1].strip()
    
    return file_contents, metadata

def make_page(in_file: pathlib.Path, header: str, footer: str, nav: str) -> str:
    html_body, metadata = parse_file(in_file)

    html_file = "<!doctype html>"
    html_file += "<html>"
    html_file += "<head>"
    html_file += f"<title>{metadata.get('title', [''])[0]}</title>"
    html_file += f"<link rel=\"stylesheet\" href=\"styles/{metadata.get('style', [''])[0]}\"/>"
    html_file += f"<link rel=\"icon\" href=\"images/{metadata.get('icon', [''])[0]}\"/>"
    html_file += "</head>"
    html_file += "<body>"
    html_file += f"<div class=\"page_header\">{header}</div>"
    html_file += f"<div class=\"page_nav\">{nav}</div>"
    html_file += f"<div class=\"page_body\">{html_body}</div>"
    html_file += f"<div class=\"page_footer\">{footer}</div>"
    html_file += "</body>"

    html_file = re.sub(r"href=\"(\S*)\.md\"", r"href=\1.html", html_file)

    return tidylib.tidy_document(html_file)[0]

if len(sys.argv) != 3:
    print("ERROR: usage: generator.py [source dir] [out dir]")
    exit()

src_dir = get_src_dir()
out_dir = get_out_dir()

print(src_dir)
print(out_dir)

if out_dir.exists():
    shutil.rmtree(out_dir)

out_dir.mkdir()
(out_dir / "images").mkdir()
(out_dir / "styles").mkdir()

# copy images (TODO: thumbnails)
for src_file in (src_dir / "images").glob("*"):
    out_file = out_dir / "images" / src_file.name
    out_file.touch()
    out_file.write_bytes(src_file.read_bytes())

# copy styles
for src_file in (src_dir / "styles").glob("*"):
    out_file = out_dir / "styles" / src_file.name
    out_file.touch()
    out_file.write_text(src_file.read_text())

header = parse_file(next((src_dir / "shared").glob("header.*")))[0]
footer = parse_file(next((src_dir / "shared").glob("footer.*")))[0]
nav = parse_file(next((src_dir / "shared").glob("nav.*")))[0]

# convert and copy pages
for src_file in (src_dir / "pages").glob("*"):
    out_file = (out_dir / src_file.name).with_suffix(".html")
    print(f"- {out_file}")

    out_file_contents = make_page(src_file, header, footer, nav)
    out_file.touch()
    out_file.write_text(out_file_contents)

