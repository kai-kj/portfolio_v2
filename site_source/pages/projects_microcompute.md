Title: microcompute
Icon: logo.jpg
Preview: assets/projects_microcompute_demo.jpeg
Tags: C Lua GLSL Vulkan
Pos: 01_02

# microcompute

A small, simple library made to run SPIR-V compute shaders, implemented using Vulkan. Lua bindings are planned.

The library will be used for any upcoming projects that require GPU computing. It simplifies the process of running computations on the GPU and is a wrapper around Vulkan.

The library also has good documentation, generated using [mini_doc_gen.py](projects_doc.md). The documentation is available [here](https://github.com/kal39/microcompute/blob/main/doc.md).

The following render of the Mandelbrot set (1920x1080, -0.7615 - 0.08459i, 1000x zoom, 500 iterations) was rendered in about 0.05 seconds, and the same render at 3840x2160 takes approximately 0.2 seconds to render.

![Mandelbrot](assets/projects_microcompute_demo.jpeg)