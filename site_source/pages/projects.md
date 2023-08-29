Title: Projects
Icon: logo.jpg

# Projects

Over the last few years, I've worked on several programming projects in my free time. The code for all these projects is open source and available on [GitHub](https://github.com/kal39).

## [VoxRen](projects_voxren.md)

![](assets/projects_01_voxren_car_gui.jpeg)

A GPU path tracer for voxel environments written in C and OpenCL. Supports lambert, metal, and light source materials. Dielectric (transparent) materials are planned for future implementation.

<div class="tech">
    <div class="item">C</div>
    <div class="item">OpenCL</div>
    <div class="item">Python</div>
</div>

## [microcompute](projects_02_microcompute.md)

![](assets/projects_microcompute_demo.jpeg)

A small, simple library made to run SPIR-V compute shaders using. Implemented using Vulkan. Lua bindings are planned.

<div class="tech">
    <div class="item">C</div>
    <div class="item">Lua</div>
    <div class="item">GLSL</div>
    <div class="item">Vulkan</div>
</div>

## [DOI Lookup](projects_03_doi.md)

![](assets/projects_doi_overview.png)

A web app to look up research articles. In addition to providing basic information about articles, the main focus of the tool is to show the relationship between articles. 

<div class="tech">
    <div class="item">HTML</div>
    <div class="item">CSS</div>
    <div class="item">JavaScript</div>
</div>

## [ptmv](projects_04_ptmv.md)

![](assets/projects_ptmv_demo.gif)

A terminal app that can display static images and play videos (both local and from YouTube) by using the Unicode character "▄" as a set of two pixels. All main features have been implemented, and it can be installed via PIP.

<div class="tech">
    <div class="item">Python</div>
</div>

## [imageToUnicode](projects_05_itu.md)

![](assets/projects_itu_demo.jpeg)

A project aimed to improve ptmv by increasing the number of Unicode characters that can be used to display an image from 1 to 19. A Python interface is planned.

<div class="tech">
    <div class="item">C</div>
    <div class="item">Python</div>
</div>

## [mini_doc_gen.py](projects_06_doc.md)

``` python
import sys, re

class T:
    def __init__(self, text): self.curr = 0; self.txt = text.splitlines(True)
    def at(self, i): return self.txt[i] if i < len(self.txt) else None
    def peek(self): return self.at(self.curr)
    def next(self): self.curr += 1; return self.at(self.curr - 1)

def d_start(l): return re.search(r"^\/\*\*\s*(\w*)", l)
def d_end(l): return re.search(r"^ \*\/", l) if l else True
def d_line(l): return re.search(r"^ ?\*? ?(.*)", l).groups()[0] + "\n"

def d_iter(txt):
    while not d_end(l := txt.next()): yield d_line(l)

def s_iter(txt):
    while txt.peek() and not d_start(txt.peek()): yield txt.next()

def t_iter(txt):
     while l := txt.next():
        if not d_start(l): continue
        match d_start(l).groups()[0]:
            case "code":
                d, s = "".join(d_iter(txt)), "".join(s_iter(txt)).strip()
                yield "\n```c\n" + s + "\n```\n\n" + d + "\n----\n"
            case "text": yield "\n" + "".join(d_iter(txt))
            case other: raise ValueError("unknown doc type found: " + other)

assert len(sys.argv) == 3, "provide 2 arguments"
open(sys.argv[2], "w").write("".join(t_iter(T(open(sys.argv[1], "r").read()))))
```

A tiny documentation generation tool written in Python. Used to generate documentation for my other projects.

<div class="tech">
    <div class="item">Python</div>
</div>