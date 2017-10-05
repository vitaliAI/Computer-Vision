#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:53:27 2017

@author: vmueller
"""

# Sharpening

# By altering our kernel we can implement sharpening, which has the effect
# of strengthening or emphasizing an image

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
cv2.imshow('Original', image)

# Creating our sharpening kernel, we don't normalize since the
# values in the matrix sum to 1

kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])

# applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

cv2.imshow('Image Sharpening', sharpened)
cv2.waitKey(0)


cv2.destroyAllWindows()a