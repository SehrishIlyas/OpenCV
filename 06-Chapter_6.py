# Reading a video 
import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")

if (cap.isOpened() == False):
    print("Error in Reading video")

#Playing

while(cap.isOpened()):
    ret, frames = cap.read()
    if ret == True:
        cv.imshow("Video", frames)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows