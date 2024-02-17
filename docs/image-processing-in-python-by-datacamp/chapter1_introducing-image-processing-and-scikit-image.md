# Chapter 1: Introducing Image Processing and scikit-image

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
