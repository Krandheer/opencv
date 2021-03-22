import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('/Users/randheerkumar/Downloads/hsv.jpg')
img=cv.resize(img, (500,500))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#grayscale histogram
gray_hist=cv.calcHist([img], [0], None, [256], [0,256])
plt.figure()
plt.title('histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim(0,256)
plt.show()

cv.imshow('img', img)
cv.waitKey(10000)
cv.destroyAllWindows()