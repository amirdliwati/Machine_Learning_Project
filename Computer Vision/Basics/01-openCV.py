import cv2

print(cv2.__version__)

img = cv2.imread('apple.jpg',1)

print(img)

cv2.imshow('first image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()