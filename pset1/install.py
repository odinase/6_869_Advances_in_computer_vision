# Ignore the pip dependecy error

import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2d
import scipy.sparse as sps
from PIL import Image

# # Package for fast equation solving
from sys import platform
print(platform)
# if platform == "linux" or platform == "linux2":
#     ! apt-get install libsuitesparse-dev
# elif platform == "darwin":
#     ! brew install suite-sparse

# ! pip3 install sparseqr
# import sparseqr