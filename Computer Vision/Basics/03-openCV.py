import numpy as np
import cv2

img = np.zeros([512, 512, 3], np.uint8)

cv2.line(img, (0,0), (256,256), (0,255,0), 10)
cv2.circle(img,(400,256),3,(255,0,0),-1)
cv2.rectangle(img,(340,10),(480,100),(0,0,255),2)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img,[pts],True,(0,0,255),2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()