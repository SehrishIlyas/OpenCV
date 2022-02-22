# Converting video to grey and black and white
# Reading a video 
import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")

#Cnvert to grey frame then binary and Playing it

while(True):
    ret, frames = cap.read()
    greyframe = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(greyframe, 127,255, cv.THRESH_BINARY)

    if ret == True:
        cv.imshow("Video", binary)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



cap.release()
cv.destroyAllWindows