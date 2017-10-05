#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:02:40 2017

@author: vmueller
"""

# Translations

# This is an affline transform that simply shifts the position of an image
# We use cv2.warpAffine to implement these transformations


import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

# Store height and width of the image
height , width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

# T is our translation matrix
T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])

# Use warpAffline to transform the image using the matrix, T
img_translation = cv2.warpAffine(image,T, (width, height))
cv2.imshow('Translation', img_translation)

cv2.waitKey()

cv2.destroyAllWindows()