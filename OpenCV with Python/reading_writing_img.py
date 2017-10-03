#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:26:09 2017

@author: vmueller
"""
# Reading and Writing and Displaying Images

import cv2
import numpy as np

# Load an image using imread specifying the path to image
input_l = cv2.imread('/Users/vmueller/Documents/Software Projects/Computer Vision/OpenCV with Python/images/input.jpg')

# Display our image Variable
cv2.imshow('Hello World', input_l)

cv2.waitKey()

cv2.destroyAllWindows()

print(input_l.shape)

# Print each Dimension of the image
print('Height of the Image: ', int(input_l.shape[0]), ' pixel')
print('Width of the Image: ', int(input_l.shape[1]), ' pixel')


# Saving Images
cv2.imwrite('output.jpg', input_l)
cv2.imwrite('output.png', input_l)



