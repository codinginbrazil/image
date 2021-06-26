#!/usr/bin/env python

from PIL import Image


if __name__ == '__main__':
    image = Image.open("./src/image/logo.png")
    image.show()

    cordinate = (300,300)
    print(image.getpixel(cordinate))
