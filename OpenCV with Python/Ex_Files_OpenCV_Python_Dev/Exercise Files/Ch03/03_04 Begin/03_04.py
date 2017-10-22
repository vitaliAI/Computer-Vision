import numpy as np
import cv2

import matplotlib.pyplot as plt

img = cv2.imread('faces.jpeg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]


hsv_split = np.concatenate((h,s,v), axis=1)

ret, min_sat =  cv2.threshold(s,40,255,cv2.THRESH_BINARY)
plt.imshow(min_sat)

ret, max_hue = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)
plt.imshow(max_hue)

cv2.imshow('Split HSV', hsv_split)

final = cv2.bitwise_and(min_sat,max_hue)
cv2.imshow('Final', final)

cv2.waitKey(0)

plt.imshow(hsv_split)

cv2.destroyAllWindows()