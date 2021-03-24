import cv2

img = cv2.imread('trail.jpg', -1)
# to draw a line arguments, starting and ending coordinates , BGM color specifications, and thickness.
img = cv2.line(img, (0,0), (237, 145), (255, 100, 49), 5)
# to draw a arrowed line arguments, starting and ending coordinates , BGM color specifications, and thickness.
img = cv2.arrowedLine(img, (237, 145), (300, 15), (0, 100, 49), 7)

# to create a rectangle, arguments, starting and ending coordinates , BGM color specifications, and thickness
# if thickness -1, fills the rectangle with the color .
img = cv2.rectangle(img, (37, 45), (300, 105), (20, 100, 9), -1 )

# to create a rectangle, arguments, center, radius, BGM color specifications, and thickness
img = cv2.circle(img, (200, 200), 30, (230, 190, 10), 9 )

# to put text in a image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Zebra', (100, 100), font, 2, (255, 255, 255), 10, cv2.LINE_AA)



cv2.imshow('Image frame', img)

cv2.waitKey(0)
cv2.destroyAllWindows()