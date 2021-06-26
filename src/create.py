#!/usr/bin/env python
""" create image """

import os
from PIL import Image


def create(size):
    image = Image.new("RGB", (size, size), (255, 255, 255) )
    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x,y), (0, 0, 0))
    return image


if __name__ == '__main__':
    image = create(500)
    image.show()
    image.save(os.path.join("./src/image/black-white.jpg"))
