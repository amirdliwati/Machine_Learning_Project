import numpy as np
import datetime
import cv2

cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(3, 3000)
# cap.set(4, 3000)
# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + '  Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0,255,255), 2)
        frame = cv2.putText(frame, datet, (10, 100), font, 1, (0,255,255), 2)
        
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
