import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, params):
    # to get the coordinates of the point
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print('x:{} and y:{}'.format(x, y))
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strXY = str(x)+', '+str(y)
    #     cv2.putText(img, strXY, (x,y), font, 0.5, (200,200,200), 1 )
    #     cv2.imshow('image', img)
    # # to get the bgr specifications
    # elif event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[y,x, 0]
    #     green = img[y,x,1]
    #     red = img[y,x,2]
    #     print('b:{}, g:{}, r:{}'.format(blue, green, red))
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strBGR = str(blue)+', '+ str(green)+ ', '+ str(red)
    #     cv2.putText(img, strBGR, (x,y), font, 0.5, (255, 255, 255), 1)
    #     cv2.imshow('image', img)
    # to draw a line between two selected points
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 2, (255, 255, 255), -1)
        points.append((x,y))
        if (len(points)>=2):
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 3)
        cv2.imshow('image', img)

    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y,x,1]
        red = img[y,x,2]
        mycColorImage = np.zeros([512,512, 3], np.uint8)
        mycColorImage[:] = [blue, green, red]
        cv2.imshow('color image', mycColorImage)
        
#img = np.zeros([512, 512, 3])
img = cv2.imread('trail.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

