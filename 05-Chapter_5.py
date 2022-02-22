## Image into Blank and white image
import cv2 as cv
from cv2 import imwrite


img = cv.imread("resources/image.png")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray_img, 127,255, cv.THRESH_BINARY)

binary = cv.resize(binary,(400,500))

imwrite("resources/img_gray.png", gray_img)
imwrite("resources/img_binary.png", binary)
