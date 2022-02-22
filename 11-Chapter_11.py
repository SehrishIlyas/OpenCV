# Converting cam to grey and black and white and saving
# Reading a video 
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#Cnvert to grey frame then binary and Playing it
# writing fromat, codec, video writer object and file output
frame_width = int(cap.get(3))
frames_height = int(cap.get(4))
out = cv.VideoWriter("resources/Cam_video.avi", cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frames_height), isColor = False)
while(True):
    ret, frames = cap.read()
    gray_frame = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    if ret == True:
        out.write(gray_frame)
        cv.imshow("Video", gray_frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cv.VideoWriter()
cap.release()
out.release()
cv.destroyAllWindows