#Joining two images
import cv2 as cv
import numpy as np

img = cv.imread("resources/img1.jpeg")

#Stacking same image


#1 Horizontal stack
hor_img = np.hstack((img, img))
#2 vertical stack
ver_img = np.vstack((img,img))

cv.imshow("Horizontal", hor_img)

cv.imshow("Vertical", ver_img)
cv.waitKey(0)
cv.destroyAllWindows()