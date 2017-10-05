#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:10:50 2017

@author: vmueller
"""
# Blurring

import cv2
import numpy as np

image = cv2.imread('images/elephant.jpg')


# Averaging done by convolution the image with a normalized box filter
# This takes the pixels under the box and replaces the central element 

blur = cv2.blur(image, (3,3))
cv2.imshow('Averaging', blur)
cv2.waitKey(0)


# Instead of Box Filter, Gaussian kernel
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

# Takes all the pixel under kernel area and central
# Element is replaced with this median value
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# Bilateral is very effective in noise removal while keeping edges sharp
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()