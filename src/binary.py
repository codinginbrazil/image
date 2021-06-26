#!/usr/bin/env python
""" Monochorme to binary """

import os
from PIL import Image


def binary(grayscale, threshold):
    w, h = grayscale.size
    img = Image.new("L", (w, h), (255) )

    for x in range(w):
        for y in range(h):
            pixel = grayscale.getpixel((x,y))
            if (pixel[0] < threshold):
                img.putpixel((x,y), (0))
    return img


if __name__ == '__main__':
    mono = Image.open("./src/image/logo-mono.png")
    
    image = binary(mono,127)
    image.show()
    image.save(os.path.join("./src/image/binary.jpg"))
    