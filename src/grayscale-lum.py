#!/usr/bin/env python

from PIL import Image


def grayscale_lum(colored):
    w, h = colored.size
    img = Image.new("P", (w, h))

    for x in range(w):
        for y in range(h):
            pixel = colored.getpixel((x,y))
            lum = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])
            img.putpixel((x,y), (lum, lum, lum))
    return img

if __name__ == '__main__':
    img_color = Image.open("image/logo.png")
    image = grayscale(img_color)
    image.show()
