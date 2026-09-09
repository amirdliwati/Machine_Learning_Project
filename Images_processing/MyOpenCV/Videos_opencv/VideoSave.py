import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
outputVideos = cv2.VideoWriter('Images_processing/MyOpenCV/Videos_opencv/outputVideo.mp4',fourcc,20.0,(640,480))

while capture.isOpened():
    rect , frame = capture.read()
    if rect==True:
        outputVideos.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
outputVideos.release()
cv2.destroyAllWindows()