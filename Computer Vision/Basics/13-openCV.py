import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')

# averaging = cv2.blur(img,(5,5))
# gblur = cv2.GaussianBlur(img,(5,5), 0)
# median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)


cv2.imshow('image',img)
# cv2.imshow('averaging',averaging)
# cv2.imshow('after gblur',gblur)
# cv2.imshow('after median',median)
cv2.imshow('after bilateralFilter',bilateralFilter)


cv2.waitKey(0)
cv2.destroyAllWindows()