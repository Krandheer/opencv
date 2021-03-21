import cv2
import numpy as np

img = np.zeros([1000, 1000, 3],dtype='uint8' )
cv2.line(img, (475,475), (850,0), (255,255,255),thickness=2)

cv2.rectangle(img, (000,000), (500, 1000), (0,255,0), thickness=cv2.FILLED)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Hello Randheer", (600,500), font, 1, (0,0,255), 2, cv2.LINE_AA)
cv2.circle(img, (img.shape[1]//2,img.shape[0]//2),40, (0,0,255), thickness=-1)

cv2.imshow('original', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
