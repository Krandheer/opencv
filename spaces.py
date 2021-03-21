import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('/Users/randheerkumar/Downloads/1.jpg')

"""plt.imshow(img)
plt.show()"""

"""bgr to hsv
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
bgr to lab
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)"""

height=400
width=400
dim=(width,height)

resized=cv.resize(img, dim)

"""b,g,r=cv.split(resized)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)"""

blur3=cv.blur(resized, (3,3))
blur5=cv.blur(resized, (3,3))
blur9=cv.blur(resized, (3,3))
cv.imshow('blur3', blur3)
cv.imshow('blur5', blur5)
cv.imshow('blur9', blur9)

cv.imshow('original', resized)
#cv.imwrite('/Users/randheerkumar/Downloads/lab.jpg', lab)
cv.waitKey(20000)
cv.destroyAllWindows()