import cv2 as cv
import numpy as np

img = cv.imread('/Users/randheerkumar/Downloads/1.jpg')

img = cv.resize(img, (500,500))

ret,thresh1 = cv.threshold(img,200,255,cv.THRESH_BINARY)

cv.imshow('original', img)
cv.imshow('thresh1', thresh1)
cv.waitKey(10000)
cv.destroyAllWindows()