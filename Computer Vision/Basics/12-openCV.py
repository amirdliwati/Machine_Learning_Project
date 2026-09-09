import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png',0)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=2)
erosion = cv2.erode(mask,kernel,iterations=2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=1) #apply erosion after that dilation
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel,iterations=2) #apply dilation after that erosion


cv2.imshow('gray image',img)
cv2.imshow('mask',mask)
cv2.imshow('after dilation',dilation)
cv2.imshow('after erosion',erosion)
cv2.imshow('after opening',opening)
cv2.imshow('after closing',closing)


cv2.waitKey(0)
cv2.destroyAllWindows()