import cv2
import numpy as np 



orginal_image = cv2.imread('Images_processing/MyOpenCV/Faces_opencv/face2.jpg')

kerenal_Filter = np.ones((5,5),np.float32)/25
dest = cv2.filter2D(orginal_image,-1,kerenal_Filter)

cv2.imshow('Image Face Filtering',dest)
cv2.imshow('Image Face orginal',orginal_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
