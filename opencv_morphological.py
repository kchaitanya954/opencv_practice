import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img_1.png',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 00, 255, cv2.THRESH_BINARY)

kernal = np.ones((2,2), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

titiles = ['image', 'mask', 'dilation','erosion', 'opening', 'closing', 'mg' ]
imgs = [ img, mask, dilation, erosion, opening, closing, mg]

for i in range(7):
    plt.subplot(2,4,i+1), plt.imshow(imgs[i], 'gray')
    plt.title(titiles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# Filters
kernal_blur = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernal_blur)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75,75c)
