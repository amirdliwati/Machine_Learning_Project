import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')

lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

hr2 = cv2.pyrUp(lr2)

cv2.imshow('image',img)
cv2.imshow('lr1',lr1)
cv2.imshow('lr2',lr2)
cv2.imshow('hr2',hr2)



cv2.waitKey(0)
cv2.destroyAllWindows()