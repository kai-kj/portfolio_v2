Title: imageToUnicode
Description: A C library to display complex images in the terminal.
Icon: logo.jpg
Preview: assets/projects_itu_demo.jpeg
Tags: C Python
Pos: 01_05

<div class="right_align">
    <img class="icon" src="assets/icon_github.svg" alt="github"/>
    <a href="https://github.com/kal39/itu">code</a>
</div>

# imageToUnicode

A C / Python library that extends the idea behind [ptmv](projects_ptmv.md), and it aims to display more complex images using unicode characters. I am eventually planning to improve ptmv using this library. A Python interface is planned.

The main difference between the graphics used in ptmv and imageToUnicode is that while ptmv only uses the Unicode character `▄`, imageToUnicode uses the following 19 characters:

```
▁ ▂ ▃ ▄ ▅ ▆ ▇

▏ ▎ ▌ ▍ ▋ ▊ ▉

▝ ▘ ▗ ▖ ▚
```

Using these characters, imageToUnicode can find the best match for a particular cluster of pixels, improving the accuracy of the final output.

Because the final goal of this project is to improve ptmv, performance is an important factor, as ptmv is also used to play videos. This is the main reason that the main algorithm is written in C. As well as being much faster than Python, C also provides direct control over memory, greatly reducing the number of wasteful operations performed. In addition, C supports true multithreading, which is the main method I used to improve performance.

Multithreading was easy to implement for each row of the output image, as this has a good balance between the number of threads and the time it takes to initialize a thread.

It is also possible to choose the level of detail wanted in the final output. This is done by restricting the number of characters allowed to be used from 19 to some specified number. The lowest level of detail uses a single character `▄`, thus outputting the same image as the current implementation of ptmv.

Here is a comparison between detail levels:

```
detail = 0 (1 character used), same as ptmv
```

![detail level 0](assets/projects_itu_detail_0.png)

```
detail = 3 (6 character used)
```

![detail level 3](assets/projects_itu_detail_3.png)

```
detail = 6 (19 character used)
```

![detail level 6](assets/projects_itu_detail_6.png)

As shown, at `detail = 6`, the image is extremely sharp, despite the entire image being made up of characters. Although the detail level can be lowered, with the optimizations currently implemented, the imageToUnicode can process images at fps suitable for ptmv.

Finally, here is what the image shown above (`detail = 6`) looks like without any colors: 

![no colour](assets/projects_itu_no_color.png)