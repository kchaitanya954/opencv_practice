import cv2
import numpy as np

img = cv2.imread('trail.jpg', cv2.IMREAD_GRAYSCALE)
def nothing(x):
    pass
cv2.namedWindow('canny')
cv2.createTrackbar('lT', 'canny', 0, 255, nothing)
cv2.createTrackbar('uT', 'canny', 0, 255, nothing)

while(1):


    l = cv2.getTrackbarPos('lT', 'canny')
    u = cv2.getTrackbarPos('uT', 'canny')

    canny = cv2.Canny(img, l, u)
    cv2.imshow('canny', canny)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
