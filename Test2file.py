import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("Tappy.avi", fourcc, 24, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow("Windowmania",frame)
        out.write(frame)

    if cv2.waitKey(1) == ord('e'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()