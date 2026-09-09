import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.jpg')

img = cv2.resize(img, (512, 512))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 20, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print('Number of contours = ' + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('image',img)
cv2.imshow('imgray',imgray)
cv2.imshow('thresh',thresh)



cv2.waitKey(0)
cv2.destroyAllWindows()