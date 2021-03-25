import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img_2.png', 0)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
_, th6 = cv2.threshold(img, 127, 255, cv2.THRESH_TRIANGLE)

titles = ['BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 'TRIANGLE']
imgs = [th1, th2, th3, th4, th5, th6]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# cv2.imshow('image', img)
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])
plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()