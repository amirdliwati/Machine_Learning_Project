import cv2

orginal_image = cv2.imread('Images_processing/MyOpenCV/face.jpg')
# cv2.imshow('face',orginal_image)
# cro = orginal_image[90:170,150:280]
# cv2.imshow('Cropping',cro)
# resized = cv2.resize(orginal_image,(200,100))
# cv2.imshow('resized',resized)

# h , w =orginal_image.shape[:2]
# center = (w//2,h//2)
# m= cv2.getRotationMatrix2D(center,-45,1.0)
# rotated = cv2.warpAffine(orginal_image,m,(w,h))
# cv2.imshow('rotated',rotated)

# blurred = cv2.GaussianBlur(orginal_image,(11,11),0)
# cv2.imshow('blurred',blurred)

output_image = orginal_image.copy()
cv2.rectangle(output_image,(150,70),(280,170),(0,0,255),3)
cv2.imshow('Drawing',output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()