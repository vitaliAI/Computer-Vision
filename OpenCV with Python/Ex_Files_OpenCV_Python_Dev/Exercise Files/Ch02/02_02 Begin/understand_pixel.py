#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 00:01:30 2017

@author: vmueller
"""

import numpy as np
import cv2
# 1 - Represent original color from the image 0 - read image as black and white
img = cv2.imread("opencv-logo.png", 1)

black = np.zeros([150,200,1], np.uint8 )
cv2.imshow("Black", black)



print(black[0,0])

cv2.waitKey(0)
cv2.destroyAllWindows()