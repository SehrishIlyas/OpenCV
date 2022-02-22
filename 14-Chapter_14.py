# Draw lines and shapes in python
import cv2 as cv
import numpy as np

#Draw canvas

img = np.zeros((600,600))
img1 = np.ones((600,600))

#print size
print("The size of our canvas is:", img.shape)
#adding colors to canvas
colored_img = np.zeros((600,600,3), np.uint8 ) #color channel
colored_img[:]= 255,0,255 #complete image
colored_img[275:325, 275:325] = 255,0,0 #part of image to be colored
#Adding line
cv.line(colored_img, (0,0), (600,600),(255,0,0), 3)
cv.line(colored_img, (600,0), (0,600),(255,0,0), 3)
cv.line(img,(0,0), (img.shape[0], img.shape[1]),(255,0,0),3)

#Adding rectangles #give thickness or just cv.filled
cv.rectangle(img,(50,100), (100,400),(255,255,255), cv.FILLED)
cv.rectangle(img,(50,100), (100,400),(255,255,255),3)

#Adding circle
cv.circle(img, (100,100),50,(255,100,0),3)

#Adding text
cv.putText(img,"Python ka chilla",(100,500), cv.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)

#Adding text to multipple lines
text = "Course: Python ka chilla, Youtube channel: Codanics, number of participants: 5000+"
wrapped_text = ['Course: Python ka chilla', 'Youtube channel: Codanics','Number of participants: 5000+']
x, y = 250,250
font_size = 0.5
font_thickness = 1

i = 0
for line in wrapped_text:
    textsize = cv.getTextSize(line, cv.FONT_HERSHEY_SIMPLEX, font_size, font_thickness)[0]

    gap = textsize[1] + 5

    y = int((img1.shape[0] + textsize[1]) / 2) + i * gap
    x = 10#for center alignment => int((img.shape[1] - textsize[0]) / 2)

    cv.putText(img1, line, (x, y), cv.FONT_HERSHEY_SIMPLEX,
                font_size, 
                (0,0,0), 
                font_thickness, 
                lineType = cv.LINE_AA)
    i +=1
cv.imshow("Black", img)
cv.imshow("White", img1)
cv.imshow("Colored", colored_img)
cv.waitKey()
cv.destroyAllWindows()