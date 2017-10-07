#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:44:25 2017

@author: vmueller
"""

import numpy as np
import cv2

color = cv2.imread("butterfly.jpg")
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg", gray)

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite('rgba.png', rgba)

rgban = cv2.merge((b,g,r))
cv2.imwrite('rgban.png', rgban)

