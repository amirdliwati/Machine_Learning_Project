import cv2

face_cascade = cv2.CascadeClassifier('Images_processing/MyOpenCV/Faces_opencv/Haar_cascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Images_processing/MyOpenCV/Faces_opencv/Haar_cascade/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('Images_processing/MyOpenCV/Faces_opencv/Haar_cascade/haarcascade_mouth.xml')

orginal_image = cv2.imread('Images_processing/MyOpenCV/Faces_opencv/face2.jpg')
gray_image = cv2.cvtColor(orginal_image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image,1.5,5)
for (x,y,w,h) in faces:
    cv2.rectangle(orginal_image,(x,y),(x+w,y+h),(0,0,255),2)
    crop_gray = gray_image[y:y+h , x:x+w]
    crop_color = orginal_image[y:y+h , x:x+w]
    eyes = eye_cascade.detectMultiScale(crop_gray)
    for (ex,ey,ew,eh) in eyes:
       cv2.rectangle(crop_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    # mouths = mouth_cascade.detectMultiScale(crop_gray)
    # for (mx,my,mw,mh) in mouths:
    #    cv2.rectangle(crop_color,(mx,my),(mx+mw,my+mh),(0.255,0),2) 


cv2.imshow('Image Face Detect',orginal_image)
#cv2.imshow('Image Face Detect',roi_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
