#!/usr/bin/env python

""" Image by PIL
    This class represents an image object. 
    To create Image objects, use the appropriate factory functions. 
    There’s hardly ever any reason to call the Image constructor directly.
        * open()
        * new()
        * frombytes()
    An instance of the Image class has the following methods. 
    Unless otherwise stated, all methods return a new instance of the Image class, 
    holding the resulting image.
    
    Docs: https://pillow.readthedocs.io/en/stable/reference/Image.html#the-image-class
"""
from PIL import Image 


if __name__ == '__main__':
    
    """ Image.open()
        Opens and identifies the given image file.
        
        This is a lazy operation; this function identifies the file, 
        but the file remains open and the actual image data is not read from the file until you try to process the data (or call the load() method).
        
        Signature: PIL.Image.open(fp, mode='r', formats=None)
            Parameters:
                * `fp` – A filename (string), pathlib.Path object or a file object. 
                The file object must implement file.read, file.seek, and file.tell methods, and be opened in binary mode.
                * `mode` – The mode. If given, this argument must be “r”.
                * `formats` – A list or tuple of formats to attempt to load the file in. 
                This can be used to restrict the set of formats checked. 
                Pass None to try all supported formats. 
                You can print the set of available formats by running python3 -m PIL or using the PIL.features.pilinfo() function.
            Returns: An Image object.
        Source: https://pillow.readthedocs.io/en/stable/_modules/PIL/Image.html#open
        Docs: https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=open#PIL.Image.open 
    """    
    image = Image.open("./image/ponte_preta/coord-21.631759,-41.758100.jpg")
    
    """ Image.show()
        Displays this image. 
        This method is mainly intended for debugging purposes.

        This method calls PIL.
        ImageShow.show() internally. 
        You can use PIL.ImageShow.register() to override its default behaviour.

        The image is first saved to a temporary file. 
        By default, it will be in PNG format.
        
        Parameters:
            title – Optional title to use for the image window, where possible.
        
        Source: https://pillow.readthedocs.io/en/stable/_modules/PIL/Image.html#Image.show
        Docs: https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=getpixel#PIL.Image.Image.show
    """
    image.show()

    cordinate = (300,300)
    
    """ Image.getpixel(xy)
        Returns the pixel value at a given position.
        Parameters
            xy – The coordinate, given as (x, y). See Coordinate System.
        Returns
            The pixel value. If the image is a multi-layer image, this method returns a tuple.
        Source: https://pillow.readthedocs.io/en/stable/_modules/PIL/Image.html#Image.getpixel 
        Docs: https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=getpixel#PIL.Image.Image.getpixel
    """
    print(image.getpixel(cordinate))
