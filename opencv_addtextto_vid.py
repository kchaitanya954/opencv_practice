import cv2
import datetime
cap= cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (0,20), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Video",frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):break

    else:
        break

cap.release()
cv2.destroyAllWindows()