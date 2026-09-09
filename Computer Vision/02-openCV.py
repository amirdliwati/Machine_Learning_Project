import numpy as np
import cv2
from matplotlib import pyplot as plt

img = np.zeros((500,500), np.uint8)
#cv2.rectangle(img, (0,250),(500,500), (255), -1)

plt.hist(img.revel(),255,[0,255])


plt.show

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()