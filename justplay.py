'''just checking out various thing here
nothing functional
'''
import cv2 as cv
import numpy as np
img = cv.imread('/Users/randheerkumar/Downloads/1.jpg')

#gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#blur=cv.GaussianBlur(img, (9,9),0)

#edge cascade
#canny=cv.Canny(blur, 125, 175)
#cv.imwrite('/Users/randheerkumar/Downloads/3.jpg', canny)

#dilating the image
#dialted=cv.dilate(canny, (9,9), iterations=6)

#translating image
"""def translate(image, x, y):
	transmat = np.float32([[1,0,x],[0,1,y]])
	print(transmat)
	dim = (image.shape[1], image.shape[0])
	return cv.warpAffine(image, transmat, dim)

translated =translate(img, 500, 500)"""

#rotation
def rotate(image, angle, rotation_point=None):
	(height, width)=image.shape[:2]
	if rotation_point==None:
		rotation_point = (width//2, height//2)

	rotMatrix=cv.getRotationMatrix2D(rotation_point, angle, 1.0)
	dim=(width, height)

	return cv.warpAffine(image, rotMatrix, dim)

rotated_image = rotate(img, -45)
rotated_rotated=rotate(rotated_image, 45)

cv.imshow('original', img)
cv.imshow('rotated_image', rotated_rotated)
cv.waitKey(10000)