## Image into Blank and white image
from cv2 import cvtColor
import cv2 as cv

img = cv.imread("resources/image.png")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray_img, 127,255, cv.THRESH_BINARY)

cv.imshow("Orignal image", img)
cv.imshow("Gray", gray_img)
cv.imshow("Black and White", binary)
cv.waitKey(0)

cv.destroyAllWindows()