#Resolution of cam

import cv2 as cv
import numpy as np

cap =  cv.VideoCapture(0)

#resolution HD(1280x720)


def hd_resolution():
    cap.set(3,1280)
    cap.set(4,720) 

def sd_resolution():
    cap.set(3,640)
    cap.set(4,480)

def fhd_resolution():
    cap.set(3,1920)
    cap.set(4,1080)
    
hd_resolution()

# writing fromat, codec, video writer object and file output
frame_width = int(cap.get(3))
frames_height = int(cap.get(4))
out = cv.VideoWriter("resources/CamHD_video.avi", cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frames_height), isColor = False)
while(True):
    ret, frames = cap.read()
    if ret == True:
        out.write(frames)
        cv.imshow("Video", frames)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cv.VideoWriter()
cap.release()
out.release()
cv.destroyAllWindows
