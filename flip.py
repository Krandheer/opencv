import cv2
import numpy as np

img = cv2.imread('/Users/randheerkumar/Desktop/ravi/randheer.jpg')
width=400
height=600
dim=(width, height)
resize = cv2.resize(img, dim)
flip = cv2.flip(resize, 0)
hero=np.concatenate((resize, flip), axis=1)

cv2.imshow('window', hero)
cv2.waitKey(10000)
cv2.destroyAllWindows()