import cv2

img = cv2.imread('/Users/randheerkumar/Desktop/ravi/randheer.jpg')
cv2.imshow('randheer', img)
print('dimension of the image: ', img.shape)

width = 400
height=400
# print(f"height is: {height}\n widht is {width} ")
dim=(width,height)
img=cv2.resize(img, dim)

cv2.imshow('window', img)


cv2.waitKey(5000)

cv2.destroyAllWindows()

"""
in cv2 dimension we have shape[0] as height and
shape[1] as width
but dimension is assigned as width first height later.
"""