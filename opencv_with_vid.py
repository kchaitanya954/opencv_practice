import cv2

cap = cv2.VideoCapture(0)

# to save a captured video
# fourcc codec can be used from https://www.fourcc.org/codecs.php
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 10, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Video frame", frame)
        cv2.imshow("Grey video frame", gray)
        # to write down the frames into out video format
        #output.write(frame)

        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
cap.release()
output.release()
cv2.destroyAllWindows()
