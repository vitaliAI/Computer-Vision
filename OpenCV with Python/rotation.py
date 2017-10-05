#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:17:16 2017

@author: vmueller
"""

 # Rotations
 
 # cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)
 
 import cv2
 import numpy as np
 
 image = cv2.imread('images/input.jpg')
 
 height, width = image.shape[:2]
 
 # Divide by 2 to rotate the image around its center
 rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
 
 rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
 
 cv2.imshow('Rotated Image', rotated_image)
 
 cv2.waitKey()
 
 cv2.destroyAllWindows()
 
 # Other option to rotate an image using transpose function
 rotate_img = cv2.transpose(image)
 
 cv2.imshow('Rotated Image - Transpose Function', rotate_img)
 
 cv2.waitKey()
 
 