import numpy as np
import cv2

img = cv2.imread('img_3.png', 0)
_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
adpTH = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('image', th)
cv2.imshow('AD_image', adpTH)

cv2.waitKey(0)
cv2.destroyAllWindows()