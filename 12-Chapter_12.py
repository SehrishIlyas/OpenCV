# Setting of camera and video

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

cap.set(10, 100) #Set brightness using key 10
cap.set(3,640) #Width
cap.set(4, 480) #Height
while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("frames", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cap.destroyAllWindows()
