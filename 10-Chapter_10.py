# convert into black and white
#step 1 import libraries
import cv2 as cv
import numpy as np
#step 2 read frames from camera
cap = cv.VideoCapture(0) #webcam no 1

if (cap.isOpened() == False):
    print("There is no error")
#step 3 display frame by frame
while(True):
    ret , frame = cap.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_img, 127,255, cv.THRESH_BINARY)


    #to display frame
    #cv.imshow("Frame", frame)
    #cv.imshow("Frame1", gray_img)
    cv.imshow("Frame2", binary)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break
  
#step 4 release and close windows easily
cap.release()
cv.destroyAllWindows