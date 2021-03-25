import numpy as np
import cv2

img = np.zeros((250, 500, 3))
img0 = np.zeros((250, 500, 3))
img1 = cv2.rectangle(img, (0,0), (250, 250), (255, 255, 255), -1)
img2 = cv2.rectangle(img0, (200,0), (300, 50), (255,255,255), -1)

bitAND = cv2.bitwise_and(img1, img2)
bitOR = cv2.bitwise_or(img1, img2)
bitXOR = cv2.bitwise_xor(img1, img2)
bitNOT = cv2.bitwise_not(img1)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('bitwise', bitXOR)

cv2.waitKey(0)
cv2.destroyAllWindows()
