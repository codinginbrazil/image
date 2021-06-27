#!/usr/bin/env python

""" SLIC
    **Parameters - [Documentação](https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.slic)**
    * image: 2D, 3D or 4D ndarray
    Input image, which can be 2D or 3D, and grayscale or multichannel (see channel_axis parameter). Input image must either be NaN-free or the NaN’s must be masked out

    * n_segments: int, optional
    The (approximate) number of labels in the segmented output image.

    * compactness: float, optional
    Balances color proximity and space proximity. Higher values give more weight to space proximity, making superpixel shapes more square/cubic. In SLICO mode, this is the initial compactness. This parameter depends strongly on image contrast and on the shapes of objects in the image. We recommend exploring possible values on a log scale, e.g., 0.01, 0.1, 1, 10, 100, before refining around a chosen value.

    Caso queira remover as marcações externa do SLIC [link](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_mask_slic.html?highlight=slic)
    [Comparison of segmentation and superpixel algorithms](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_segmentations.html#sphx-glr-auto-examples-segmentation-plot-segmentations-py)
    https://docs.opencv.org/3.0-beta/modules/ximgproc/doc/superpixels.html
"""

import matplotlib.pyplot as plt
import numpy as np

from skimage.data import astronaut
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io


""" Carrega a imagem por intermédio de uma URL"""
img = io.imread('https://raw.githubusercontent.com/sswellington/2PLA/main/image/example_1_1PLA.png')


segments_slic = slic(img, n_segments=250, compactness=10, sigma=1)
print(f"SLIC number of segments: {len(np.unique(segments_slic))}")

"""Exibição da imagem
    Resolução da imagem de saída
    * Processo que ocupa maior tempo de processamento
    * Resolução adequada para teste: 200
    * Resolução adequada para comparação de resultados: 300 dpi ou mais
    ```
        plt.gcf().set_dpi(200) 
    ```
"""

plt.imshow(mark_boundaries(img, segments_slic))

plt.gcf().set_dpi(200) 
plt.show()
