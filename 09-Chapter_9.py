# Hoe to cspture a webcam in python
#step 1 import libraries
import cv2 as cv
import numpy as np
#step 2 read frames from camera
cap = cv.VideoCapture(0) #webcam no 1

if (cap.isOpened() == False):
    print("There is no error")
#step 3 display frame by frame
while(cap.isOpened()):
    ret , frame = cap.read()
    if ret  == True:
        #to display frame
        cv.imshow("Frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#step 4 release and close windows easily
cap.release()
cv.destroyAllWindows