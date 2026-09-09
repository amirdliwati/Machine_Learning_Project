import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg',0)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

compine_sobel_x_and_y = cv2.bitwise_or(sobel_x, sobel_y)

canny = cv2.Canny(img, 100, 200)

cv2.imshow('image',img)
cv2.imshow('laplacian',lap)
cv2.imshow('sobel_x',sobel_x)
cv2.imshow('sobel_y',sobel_y)
cv2.imshow('compine_sobel_x_and_y',compine_sobel_x_and_y)
cv2.imshow('canny',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()