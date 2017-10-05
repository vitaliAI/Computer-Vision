#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:38:26 2017

@author: vmueller
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

image = cv2.imread('images/input.jpg')
print('This image is: ', type(image),
      ' with dimensions: ', image.shape)


# Pull out the x and y sizes and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]

region_select = np.copy(image)

# Define a Triangle region of interest
# Keep in mind that x = 0, y = 0 is in the upper left in image processing

left_bottom = [0, 500]
right_bottom = [900, 300]
apex = [400, 0]


# Fit lines y = Ax + B to identify the 3 sided region of interest
# np.polyfit() returns the coefficient [A,B] of the fit

fit_left = np.polyfit((left_bottom[0],apex[0]),(left_bottom[1],apex[1]),1)
fit_right = np.polyfit((right_bottom[0],apex[0]),(right_bottom[1],apex[1]),1)
fit_bottom = np.polyfit((left_bottom[0],right_bottom[0]),(left_bottom[1],right_bottom[1]),1)

# Find the region inside the lines
XX, YY = np.meshgrid(np.arange(0,xsize), np.arange(0,ysize))

region_treshold = (YY > XX*fit_left[0] + fit_left[1]) & \
                  (YY > XX*fit_right[0] + fit_right[1]) & \
                  (YY < XX*fit_bottom[0] + fit_bottom[1])
                  
# Color Pixels RED which are inside the region of interest
region_select[region_treshold] = [255,0,0]

cv2.imshow('Region Selected', region_select)


cv2.destroyAllWindows()

