# SWZLv2
A simple lossless image format and compact single-file library for it made because uhhh idk 
i just wanted to make an image format. So yeah, not really designed for efficiency (although 
it does make an effort to be somewhat small), but for simplicity.

The standard file extensions for this format are `.swzl2` and `.sw2l`.

## File Spec
- There's a magic string at the start of the file that contains the letters "SM" and a bit
that dictates whether the image stores alpha data or not.

- The width of the image is then specified after the magic string as a little-endian uint32.
Each pixel is described by its hex color value (and 8-bit alpha value if the image stores alpha data).
RGB mode takes up 3 bytes per pixel, RGBA mode takes 4.

- Height is row-based, so every {image width} pixels, the decoder assumes the next row of pixels.

As of now, no compression is implemented whatsoever.

## How To Use
On Unix-like:
```
./install.sh
```
or, on Windows:
```
makecommand path\to\swzl2
```

This repo includes two things:
- `libswzl2`: The library itself so you can use it anywhere you want.
- `swzlr` (Swizzler): A CLI for encoding/decoding swzl2 images.

### CLI Usage
```
# Encode/convert images to SWZLv2
swzlr encode image.png image.swzl2

# Decode swzl2 to another file format
swzlr decode image.swzl2 image.png

# Inspect swzl2 image properties
swzlr inspect image.swzl2
```

## Library implementations
### libswzl2.py
Main SWZLv2 library.
Supports:
- `.encode`: Yes
- `.decode`: Yes
- `.inspect`: Yes
- RGBA mode: Yes

### swzl2.js
SWZLv2 library rewritten in JavaScript for browser environments.
Supports:
- `.encode`: Yes
- `.decode`: Yes
- `.inspect`: Yes
- RGBA mode: Yes

Additionally, swzl2.js auto-decodes and renders .swzl2 images inside `<img>` 
tags when embedded into a website.

### xswzl2.c
SWZLv2 viewer implemented in Xlib.
Supports:
- `.encode`: No; viewer only
- `.decode`: Yes
- `.inspect`: No
- RGBA mode: Yes

## Where SWZLv1?
SWZL was a scrapped custom image format for the Nintendo DS port of the 
[Scratch Everywhere!](https://github.com/ScratchEverywhere/ScratchEverywhere) project (which i'm a dev in,
you should go check it out!). This internally has not much to do with that except for the name, and I just 
thought that SWZL sounded too cool to scrap it.
