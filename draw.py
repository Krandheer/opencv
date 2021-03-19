import cv2
import numpy as np

img = np.zeros([1000, 1000, 3],dtype='uint8' )
cv2.line(img, (0,0,), (475,475), (255,0,0), 2)
cv2.line(img, (475,475), (850,0), (255,0,0), 2)

cv2.rectangle(img, (200,150), (300, 300), (255,0,0), 3)


font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "hello randheer", (10,800), font, 1, (0,0,255), 2, cv2.LINE_AA)
cv2.imshow('original', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
