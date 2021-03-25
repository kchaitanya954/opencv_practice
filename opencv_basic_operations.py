import numpy as np
import cv2

img = cv2.imread('trail.jpg')
print(img.shape)

b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

# to crop a part of a image
crow = img[80:100, 100:140]
# to replace a part of a image
img[160:180, 240:280] = crow

img2 = cv2.imread('shiva.png')
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512, 512))

# to add two images with weights
add = cv2.addWeighted(img, 0.5, img2, 0.5, 0)

cv2.imshow('image', add)
cv2.waitKey(0)
cv2.destroyAllWindows()