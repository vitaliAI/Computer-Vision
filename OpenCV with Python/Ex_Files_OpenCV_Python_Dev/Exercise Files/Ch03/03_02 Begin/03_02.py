import numpy as np
import cv2
import matplotlib.pyplot as plt

# Simple Thresholding

bw = cv2.imread('detect_blob.png',0)

plt.imshow(bw)

height, width = bw.shape

cv2.imshow('Original BW', bw)

binary = np.zeros([height, width,1], 'uint8')

threshold = 85

for row in range(0, height):
    for col in range(0,width):
        if bw[row][col] > threshold:
            binary[row][col] = 255
            
            

ret, thresh = cv2.threshold(bw, threshold, 255, cv2.THRESH_BINARY)
plt.imshow(thresh)

cv2.imshow('CV Threshold', thresh)

cv2.imshow('Slow Binary', binary)

cv2.waitKey(0)

cv2.destroyAllWindows()