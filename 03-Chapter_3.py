## grey scale conversion
from cv2 import cvtColor
import cv2 as cv

img = cv.imread("resources/image.png")
img = cv.resize(img,(800,600))
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("pehli image", img)
cv.imshow("dosri image", gray_img)
cv.waitKey(0)

cv.destroyAllWindows()