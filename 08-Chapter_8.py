# Converting video to grey and black and white
# Reading a video 
import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")

#Cnvert to grey frame then binary and Playing it
# writing fromat, codec, video writer object and file output
frame_width = int(cap.get(3))
frames_height = int(cap.get(4))
out = cv.VideoWriter("resources/Out_video.avi", cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frames_height),isColor=False)
while(True):
    ret, frames = cap.read()
    greyframe = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(frames, 127,255, cv.THRESH_BINARY)
    
    if ret == True:
        out.write(greyframe)
        cv.imshow("Video", greyframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



cap.release()
out.release()
cv.destroyAllWindows