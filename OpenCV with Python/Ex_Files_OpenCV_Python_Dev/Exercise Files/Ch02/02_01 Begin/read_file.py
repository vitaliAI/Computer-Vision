#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 23:51:41 2017

@author: vmueller
"""

import numpy as np
import cv2

img = cv2.imread('opencv-logo.png')

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.imwrite("output.jpg", img)

cv2.destroyAllWindows()