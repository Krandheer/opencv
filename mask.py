import cv2 as cv
import numpy as np

img = cv.imread('/Users/randheerkumar/Downloads/1.jpg')

img=cv.resize(img, (500,500))
cv.imshow('original',img)

blank=np.zeros(img.shape[:2], dtype ='uint8')
cv.imshow('blank', blank)

mask=cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2-100), 100, 255, -1)
cv.imshow('mask', mask) 

masked=cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(5000)
cv.destroyAllWinddows()