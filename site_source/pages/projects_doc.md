Title: mini_doc_gen.py
Description: A tiny Python script that generates documentation in Markdown.
Icon: logo.jpg
Preview: assets/projects_doc_demo.png
Tags: Python
Pos: 01_06

<div class="right_align">
    <img class="icon" src="assets/icon_github.svg" alt="github"/>
    <a href="https://gist.github.com/kal39/26e870d9436c06b2fece78f19a755fbc">code</a>
</div>

# `mini_doc_gen.py`

A tiny Python script (only 30 loc) that, given a C file, generates documentation for it. The output is a markdown file, making it ideal for use with GitHub. The full code is shown below: 

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

[microcompute](projects_microcompute.md) uses this tool to generate documentation. The output can be seen [here](https://github.com/kal39/microcompute/blob/main/doc.md).