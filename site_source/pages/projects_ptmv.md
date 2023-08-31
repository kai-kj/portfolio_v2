Title: ptmv
Icon: logo.jpg
Preview: assets/projects_ptmv_demo.gif
Tags: Python
Pos: 01_04

# ptmv

A terminal app that can display static images and play videos (both local and from YouTube) by using the Unicode character `▄` as a set of two pixels. All main features have been implemented, and it can be installed via PIP.

The entire app is written in Python, and it is also very simple, compared to the other projects I've worked on. It has also been optimized in several ways, in order to still play videos at a high fps, even on a high "resolution".

The way the app works is extremely simple. It uses the Unicode character "▄", as two vertically stacked pixels, and the color of the two pixels is set by changing the foreground and background colors. Using this technique, it is possible to cram a relatively large number of pixels into a terminal.

One of the main forms of optimizations implemented was to only update pixels that changed since the last frame. This can be done by moving the cursor to the pixels that have been changed instead of printing a single, long, string with all the pixels. However, because cursor movement is not extremely fast, adjacent pixels are drawn at once.

Here's the app in action:

![demo](assets/projects_ptmv_demo.gif)

This app can be installed by using [pip](https://pypi.org/project/ptmv/):

```
pip install ptmv
```

For detailed install instructions, visit the [GitHub page](https://github.com/kal39/ptmv). 