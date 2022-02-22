# Reading and displaying an image

import cv2 as cv

img = cv.imread("resources/image.png")

cv.imshow("pehli image", img)
cv.waitKey(0)

cv.destroyAllWindows()