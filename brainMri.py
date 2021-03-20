import numpy as np
import cv2
import pydicom as dicom

#to run change the path of image to where image is placed
ds=dicom.dcmread('/Users/randheerkumar/Desktop/sems/lastsem/bml735/ass3/SWI_MRI.dcm')
dcm_sample=ds.pixel_array*128

#lap(image)
kernel = np.array([[-1, -1, -1] , [-1, 8, -1] , [-1, -1, -1]])
laplacian_kernel = cv2.filter2D(dcm_sample, ddepth=cv2.CV_64F, kernel=kernel)

high_boost1 = 1*dcm_sample-laplacian_kernel
high_boost2 = 2*dcm_sample-laplacian_kernel
high_boost10 = 10*dcm_sample-laplacian_kernel
high_boost20 = 20*dcm_sample-laplacian_kernel

height=250
width=250
dim=(width, height)

dcm_sample = cv2.resize(dcm_sample, dim)
high_boost1 = cv2.resize(high_boost1, dim)
high_boost2 = cv2.resize(high_boost2, dim)
high_boost10 = cv2.resize(high_boost10, dim)
high_boost20 = cv2.resize(high_boost20, dim)

cv2.imshow('original dicom image',dcm_sample)
cv2.imshow('high boost1',high_boost1)
cv2.imshow('high boost2',high_boost2)
cv2.imshow('high boost10',high_boost10)
cv2.imshow('high boost20',high_boost20)

cv2.waitKey(30000)
cv2.destroyAllWindows()
