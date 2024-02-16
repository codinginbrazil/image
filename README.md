# Processamento de imagem

## [Image Processing in Python](https://app.datacamp.com/learn/courses/image-processing-in-python)
Images are everywhere! We live in a time where images contain lots of information, which is sometimes difficult to obtain. 
This is why image pre-processing has become a highly valuable skill, applicable in many use cases. 
In this course, you will learn to process, transform, and manipulate images at your will, even when they come in thousands. 
You will also learn to restore damaged images, perform noise reduction, smart-resize images, count the number of dots on a dice, apply facial detection, and much more, using scikit-image. 
After completing this course, you will be able to apply your knowledge to different domains such as machine learning and artificial intelligence, machine and robotic vision, space and medical image analysis, retailing, and many more. 
Take the step and dive into the wonderful world that is computer vision!

### Introducing Image Processing and scikit-image
Jump into digital image structures and learn to process them! 
Extract data, transform and analyze images using NumPy and Scikit-image. 
With just a few lines of code, you will convert RGB images to grayscale, get data from them, obtain histograms containing very useful information, and separate objects from the background!

#### RGB to Grayscale
```python
''' Instructions:
    - Import the data and color modules from Scikit image. The first module provides example images, and the second, color transformation functions.
    - Load the rocket image.
    - Convert the RGB-3 rocket image to grayscale.
'''

# Import the modules from skimage
from skimage import data

# (Color)[https://scikit-image.org/docs/stable/api/skimage.color.html]
# (RGB to Grayscale)[https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_rgb_to_gray.html#sphx-glr-auto-examples-color-exposure-plot-rgb-to-gray-py]
from skimage.color import rgb2gray

# Load the rocket image
rocket = data.rocket()

# Convert the image to grayscale
gray_scaled_rocket = rgb2gray(rocket)

# Show the original image
show_image(rocket, 'Original RGB image')

# Show the grayscale image
show_image(gray_scaled_rocket, 'Grayscale image')
```

#### Flipping

#### Histograms
- [matplotlib - histogram](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)

#### Thresholding
##### Apply global thresholding
```python
''' Instructions:
    - Import the otsu threshold function.
    - Turn the image to grayscale.
    - Obtain the optimal threshold value of the image.
    - Apply thresholding to the image.
'''

# Import the otsu threshold function
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu

# Make the image grayscale using rgb2gray
chess_pieces_image_gray = rgb2gray(chess_pieces_image)

# Obtain the optimal threshold value with otsu
thresh = threshold_otsu(chess_pieces_image_gray)

# Apply thresholding to the image
binary = chess_pieces_image_gray > thresh

# Show the image
show_image(binary, 'Binary image')
```

##### Otsu threshold
```python
# Obtain the optimal global thresh value of the image, and apply global thresholding.
# Import the otsu threshold function
from skimage.filters import threshold_otsu


# Obtain the optimal otsu global thresh value
global_thresh = threshold_otsu(page_image)

# Obtain the binary image by applying global thresholding
binary_global = page_image > global_thresh

# Show the binary image obtained
show_image(binary_global, 'Global thresholding')
```

##### local threshold function
```python
# Import the local threshold function
from skimage.filters import threshold_local

# Set the block size to 35
block_size = 35

# Obtain the optimal local thresholding
local_thresh = threshold_local(page_image, block_size, offset=10)

# Obtain the binary image by applying local thresholding
binary_local = page_image > local_thresh

# Show the binary image
show_image(binary_local, 'Local thresholding')
```

##### other methods
scikit-image provides us with a function to check multiple methods and see for ourselves what the best option is. 
It returns a figure comparing the outputs of different global thresholding methods.

```python
''' Instructions:
    - Import the try all function.
    - Import the rgb to gray convertor function.
    - Turn the fruits image to grayscale.
    - Use the try all method on the resulting grayscale image.
'''
# Import the try all function
import matplotlib.pyplot as plt

# Import the rgb to gray convertor function 
from skimage import data
from skimage.color import rgb2gray
from skimage.filters import try_all_threshold as tat 

#img = data.astronaut()
# Turn the fruits_image to grayscale
grayscale = rgb2gray(fruits_image)

# Use the try all method on the resulting grayscale image
fig, ax = tat(grayscale, verbose=False)

# Show the resulting plots
plt.show()
```
##### Binary image
```python
''' Instructions
    Import the appropriate thresholding and rgb2gray() functions.
    Turn the image to grayscale.
    Obtain the optimal thresh.
    Obtain the binary image by applying thresholding.
'''
# Import threshold and gray convertor functions
from skimage.filters import threshold_otsu as otsu
from skimage.color import rgb2gray

# Turn the image grayscale
gray_tools_image = rgb2gray(tools_image)

# Obtain the optimal thresh
thresh = otsu(gray_tools_image)

# Obtain the binary image by applying thresholding
binary_image = gray_tools_image > thresh

# Show the resulting binary image
show_image(binary_image, 'Binarized image')
```

- https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.threshold_otsu
- https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.threshold_local

---

### Filters, Contrast, Transformation and Morphology
You will learn to detect object shapes using edge detection filters, improve medical images with contrast enhancement and even enlarge pictures to five times its original size! 
You will also apply morphology to make thresholding more accurate when segmenting images and go to the next level of processing images with Python.

#### Filters
##### Edge detection
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

##### Blurring to reduce noise
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

#### Contrast

##### Histogram Equalization
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

##### Add some impact and contrast
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

#### Transformation
##### Aliasing, rotating and rescaling

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

#### Morphology

---

### Image restoration, Noise, Segmentation and Contours
So far, you have done some very cool things with your image processing skills! In this chapter, you will apply image restoration to remove objects, logos, text, or damaged areas in pictures! 
You will also learn how to apply noise, use segmentation to speed up processing, and find elements in images by their contours. 

#### Image restoration

#### Noise
#### Segmentation
#### Contours

---

### Advanced Operations, Detecting Faces and Features
After completing this chapter, you will have a deeper knowledge of image processing as you will be able to detect edges, corners, and even faces! 
You will learn how to detect not just front faces but also face profiles, cat, or dogs. 
You will apply your skills to more complex real-world applications. 
Learn to master several widely used image processing techniques with very few lines of code! 

#### Advanced Operations
#### Detecting Faces
--- 

## Documentation
- [Pillow](https://pillow.readthedocs.io/en/stable/)
    - [Documentation](https://pillow.readthedocs.io/en/stable/reference/index.html)

## Referência

- BARELLI, Felipe. Introdução à Visão Computacional: Uma abordagem prática com Python e OpenCV. Casa do Código, 2018.
- GONZALEZ, Rafael C.; WOODS, Richard E. Processamento de imagens digitais. Editora Blucher, 2000.
- SONKA, Milan; HLAVAC, Vaclav; BOYLE, Roger. Image processing, analysis, and machine vision. Nelson Education, 2014.