import cv2 as MyOpenCVlib


orginal_image = MyOpenCVlib.imread('images_processing/MyOpenCV/face.jpg',0)

# MyOpenCVlib.imshow('Image Face',orginal_image)
# MyOpenCVlib.waitKey(0)
# MyOpenCVlib.imwrite('images_processing/MyOpenCV/face.png',orginal_image)
# MyOpenCVlib.destroyAllWindows()

# px = orginal_image[100,100]
# print(px)

edges = MyOpenCVlib.Canny(orginal_image,100,200,apertureSize = 3)

#MyOpenCVlib.imshow('Image Face',orginal_image)
MyOpenCVlib.imshow('edges',edges)
MyOpenCVlib.waitKey(0)
MyOpenCVlib.destroyAllWindows()

