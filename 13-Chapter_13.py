#Basic Functions or Manipulations in OpenCV

from msilib.schema import Binary
import cv2 as cv
import numpy as np

img = cv.imread("resources/img1.jpeg")
img = cv.resize(img, (500,700))
#Resize
resized_img = cv.resize(img,(450,250))
# Grey
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#Black AND White
(thresh, binary) = cv.threshold(grey_img, 127,255, cv.THRESH_BINARY)
#Blured Image
blurr_img = cv.GaussianBlur(img, (7,7), 0)
#Edge Detection
edge_img = cv.Canny(img, 53,53)
#Thickness of lines
mat_kernal = np.ones((7,7), np.uint8) # or (7,7) or (23,23)
dilated_img = cv.dilate(edge_img,(mat_kernal), iterations = 1)
# Make thinner outlines
ero_img = cv.erode(dilated_img, mat_kernal, iterations=1)
#Cropping we will use numpy not openCV
print("The szie of our image is: ", img.shape)
cropped_img = img[150:500, 100:500]


cv.imshow("Orignal", img)
cv.imshow("Resized", resized_img)
cv.imshow("Binary", binary)
cv.imshow("Grey", grey_img)
cv.imshow("Blurr", blurr_img)
cv.imshow("Edge", edge_img)
cv.imshow("Dilation", dilated_img)
cv.imshow("Erotsion", ero_img)bngktfv
cv.imshow("Cropped Image", cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()