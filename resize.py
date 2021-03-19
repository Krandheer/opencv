import cv2
import numpy as np

img = cv2.imread('/Users/randheerkumar/Desktop/ravi/randheer.jpg')

print(f'dimensions of original image: {img.shape}')

scale = 150
width = int(img.shape[1]*scale/100)
height = int(img.shape[0]*scale/100)

dim=(width, height)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
print(f'dimensions of resized image: {resized.shape}')


cv2.imshow('original', img)
cv2.imshow('resized', resized)
cv2.waitKey(10000)
cv2.destroyAllWindows()