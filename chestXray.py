import numpy as np
import cv2
from matplotlib import pyplot as plt

#to run change the path of image to where image is placed
img = cv2.imread('/Users/randheerkumar/Desktop/sems/lastsem/bml735/ass3/ChestXray.png')

height=300
width=300
dim=(width, height)

#laplacian filter kernel
kernel = np.array([[-1, -1, -1] , [-1, 8, -1] , [-1, -1, -1]])
laplacian_kernel = cv2.filter2D(img, ddepth=cv2.CV_64F, kernel=kernel)

#gaussian smoothening
smoothened=cv2.GaussianBlur(img,(3,3),0)

#laplacian of gaussian
laplacian_of_gaussian = cv2.filter2D(smoothened, ddepth=cv2.CV_64F, kernel=kernel)

f, axarr = plt.subplots(nrows=1,ncols=3)
plt.sca(axarr[0]); 
plt.imshow(img); plt.title('original')
plt.sca(axarr[1]); 
plt.imshow(laplacian_kernel); plt.title('laplacian_kernel')
plt.sca(axarr[2]); 
plt.imshow(laplacian_of_gaussian); plt.title('laplacian_of_gaussian')
plt.show()