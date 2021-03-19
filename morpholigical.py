"""
what is opening of image, top hat, black hat, closing
of image in cv2 ?
erosion?
aspect ratio ?
"""

import cv2
import numpy as np

img = cv2.imread('/Users/randheerkumar/Desktop/ravi/randheer.jpg')
width=400
height=600
dim=(width, height)
resize = cv2.resize(img, dim)

kernel = np.ones((5,5), dtype='uint8')

# erosion=cv2.erode(resize, kernel, iterations=1)
# dilation = cv2.dilate(resize, kernel, iterations=1)
# opening = cv2.morphologyEx(resize, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(resize, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(resize, cv2.MORPH_GRADIENT, kernel)

Hori = np.concatenate((resize, gradient), axis=1)


cv2.imshow('HORIZONTAL', Hori) 

cv2.waitKey(0)
cv2.destroyAllWindows()