import numpy as np
import imutils
import cv2

# create 3 windows 
cv2.namedWindow("Gray")
cv2.namedWindow("HSV")

# load and resize the image
image = cv2.imread("../Images/cat.jpeg", 1)
image = cv2.resize(image, (1000,650))

# convert image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# display both images
cv2.imshow("HSV", image_hsv)
cv2.imshow("Gray", image_gray)

# wait until key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()