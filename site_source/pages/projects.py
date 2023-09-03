import pathlib
import markdown
import re

src_dir = pathlib.Path(globals()["src_dir"])

src_files = list((src_dir / "pages").glob("*"))
src_files = [(f, (globals()["parse_file"])(f)[1]) for f in src_files if "projects_" in f.name]
src_files.sort(key=lambda f: f[1].get('pos', [''])[0])
src_files = [f[0] for f in src_files]

output = "Title: Projects\n"
output += "Description: A list of projects I've worked on in my free time.\n"
output += "Icon: logo.jpg\n"
output += "Pos: 01_00\n\n"
output += "# Projects\n"
output += "Over the last few years, I've worked on several programming projects in my free time. The code for all these projects is open source and available on [GitHub](https://github.com/kal39)."

for src_file in src_files:
    md = markdown.Markdown(extensions = ["meta"])
    md.convert(src_file.read_text())

    title = md.Meta.get('title', [''])[0]
    preview = md.Meta.get('preview', [''])[0]
    desc = re.match(r"^[\s\S]*#.*\s*(.*)", src_file.read_text()).groups()[0]
    tech = md.Meta.get('tags', [''])[0]
    link = src_file.name.replace(".md", ".html")

    output += "\n"
    output += f"<h2><a href=\"{link}\">{title}</a></h2>\n"
    output += f"<a href=\"{link}\"><img alt=\"preview\" src=\"{preview}\"></a>"

    if len(tech) != 0:
        output += f"<div style=\"display: flex; justify-content: center;\">"
        for t in tech.split():
            output += f"<code>{t}</code>&nbsp;"
        output += "</div>\n\n"

    output += f"{desc}\n"