## Reading an image and resizing it
import numpy as np
import cv2 as cv

img = cv.imread("resources/image.png")
img1 = cv.resize(img,(600,600))
cv.imshow("pehli image", img)
cv.imshow("dosri image", img1)
cv.waitKey(0)

cv.destroyAllWindows()