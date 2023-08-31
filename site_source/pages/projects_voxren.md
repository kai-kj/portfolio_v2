Title: VoxRen
Description: A GPU path tracer for voxel environments written in C and OpenCL.
Icon: logo.jpg
Preview: assets/projects_voxren_car_gui.jpeg
Tags: C Python OpenCL RayLib
Pos: 01_01

<div class="right_align">
    <img class="icon" src="assets/icon_github.svg" alt="github"/>
    <a href="https://github.com/kal39/VoxRen">code</a>
</div>

# VoxRen

A GPU path tracer for voxel environments written in C and OpenCL. Supports lambert, metal, and light source materials. Dielectric (transparent) materials are planned for future implementation. Contains a full GUI that helps the user easily modify the scene, and a Python module was written so that a scene can be easily created using scripts.

All GPU-side code was written using OpenCL so that it would run on a wider range of hardware, like my laptop (with Intel integrated graphics), compared to CUDA. Most CPU-side code (the GUI and various other processes) was written in C, except the scene-generation code that was written in Python.

The GUI was implemented using [RayLib](https://www.raylib.com/), a library that provides a large number of features aimed at game development. All GUI components (windows, buttons, text inputs) were implemented from scratch using basic features from the library. Although the GUI is far from perfect, building an entire GUI system from scratch taught me a lot about GUIs and graphics in general. This is a screenshot of the GUI in action: 

![GUI](assets/projects_voxren_iberia_gui.jpeg)

The GUI allows the user to perform several actions such as:

- Select a material type, color, and properties, and place it in the scene using the mouse
- Set various camera parameters, such as position orientation, exposure, etc
- Change the color and brightness of the background
- Change the movement speed and mouse sensitivity

The Python module can be used in scripts to easily create large complex scenes. It can also be used to visualize data. For example, using heightmap data 3D maps can be generated:

![Iberia](assets/projects_voxren_iberia.jpeg)

![SEA](assets/projects_voxren_sea.jpeg)

More conventional scenes can also be rendered, such as this car:

![car](assets/projects_voxren_car.jpeg)

As this is now a relatively old project, I am planning to remake it using new techniques and knowledge I've acquired over the last couple of years.