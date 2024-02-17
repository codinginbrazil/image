# Chapter 2: Filters, Contrast, Transformation and Morphology

You will learn to detect object shapes using edge detection filters, improve medical images with contrast enhancement and even enlarge pictures to five times its original size! 
You will also apply morphology to make thresholding more accurate when segmenting images and go to the next level of processing images with Python.

## Filters
### Edge detection
- Sobel
```python
''' Instructions
    - Import the color module so you can convert the image to grayscale.
    - Import the sobel() function from filters module.
    - Make soaps_image grayscale using the appropriate method from the color module.
    - Apply the sobel edge detection filter on the obtained grayscale image soaps_image_gray.
'''
# Import the color module
from skimage import color

# Import the filters module and sobel function
from skimage.filters import sobel

# Make the image grayscale
soaps_image_gray = color.rgb2gray(soaps_image)

# Apply edge detection filter
edge_sobel = sobel(soaps_image_gray)

# Show original and resulting image to compare
show_image(soaps_image, "Original")
show_image(edge_sobel, "Edges with Sobel")
```

### Blurring to reduce noise
- Gaussian filter 
```python
''' Instructions
    - Import the Gaussian filter.
    - Apply the filter to the building_image, set the multichannel parameter to the correct value.
    - Show the original building_image and resulting gaussian_image.
'''
# Import Gaussian filter 
from skimage.filters import gaussian 

# Apply filter
gaussian_image = gaussian(building_image, multichannel=True)

# Show original and resulting image to compare
show_image(building_image, "Original")
show_image(gaussian_image, "Reduced sharpness Gaussian")
```

- https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.sobel

---

## Contrast

### Histogram Equalization
```python
''' Instructions
    - Import the required Scikit-image module for contrast.
    - Show the histogram from the original x-ray image chest_xray_image, using the hist() function.
    - Use histogram equalization on chest_xray_image to obtain the improved image and load it as xray_image_eq.
    - Show the resulting improved image xray_image_eq.
'''
# Import the required module
from skimage import exposure

# Show original x-ray image and its histogram
show_image(chest_xray_image, 'Original x-ray')

plt.title('Histogram of image')
plt.hist(chest_xray_image.ravel(), bins=256)
plt.show()

# Use histogram equalization to improve the contrast
xray_image_eq =  exposure.equalize_hist(chest_xray_image)

# Show the resulting image
show_image(xray_image_eq, 'Resulting image')
```

```python
''' Instructions
    - Import the required module from scikit-image.
    - Use the histogram equalization function from the module previously imported.
    - Show the resulting image.
'''
# Import the required module
from skimage import exposure

# Use histogram equalization to improve the contrast
image_eq = exposure.equalize_hist(image_aerial)

# Show the original and resulting image
show_image(image_aerial, 'Original')
show_image(image_eq, 'Resulting image')
```

### Equalize adapthist
```python
''' Instructions
    - Import the module that includes the Contrast Limited Adaptive Histogram Equalization (CLAHE) function.
    - Obtain the image you'll work on, with a cup of coffee in it, from the module that holds all the images for testing purposes.
    - From the previously imported module, call the function to apply the adaptive equalization method on the original image and set the clip limit to 0.03.
'''
# Import the necessary modules
from skimage import data, exposure

# Load the image
original_image = data.coffee()

# Apply the adaptive equalization on the original image
adapthist_eq_image = exposure.equalize_adapthist(original_image, clip_limit=0.03)

# Compare the original image to the equalized
show_image(original_image)
show_image(adapthist_eq_image, '#ImageProcessingDatacamp')
```

- https://scikit-image.org/docs/stable/api/skimage.exposure.html
- https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_equalize.html#histogram-equalization

---

## Transformation
### Aliasing, rotating and rescaling

```python 
# Import the module and the rotate and rescale functions
from skimage.transform import rotate, rescale

scale = 1/4

# Rotate the image 90 degrees clockwise 
rotated_cat_image = rotate(image_cat, -90)

# Rescale with anti aliasing
rescaled_with_aa = rescale(rotated_cat_image, scale, anti_aliasing=True, multichannel=True)

# Rescale without anti aliasing
rescaled_without_aa = rescale(rotated_cat_image, scale, anti_aliasing=False, multichannel=True)

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")
```

```python
''' Instructions
    - Import the module and function to resize.
    - Set the proportional height and width so it is half the image's height size.
    - Resize using the calculated proportional height and width.
'''
# Import the module and function
from skimage.transform import resize

# Set proportional height so its half its size
height = int(dogs_banner.shape[0] / 2)
width = int(dogs_banner.shape[1] / 2)

# Resize using the calculated proportional height and width
image_resized = resize(dogs_banner, (height, width), anti_aliasing=True)

# Show the original and resized image
show_image(dogs_banner, 'Original')
show_image(image_resized, 'Resized image')
```

---

## Morphology
### Erosion
```python
# Import the morphology module from skimage
from skimage import morphology

# Apply the morphological operation for eroding away the boundaries of regions of foreground pixels.
# Obtain the eroded shape 
eroded_image_shape = morphology.binary_erosion(upper_r_image) 

# See results
show_image(upper_r_image, 'Original')
show_image(eroded_image_shape, 'Eroded image')
```

### Dilation
```python
# Import the module
from skimage import morphology

# Obtain the dilated image 
dilated_image = morphology.binary_dilation(world_image)

# See results
show_image(world_image, 'Original')
show_image(dilated_image, 'Dilated image')
```
