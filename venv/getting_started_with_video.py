import cv2
import datetime

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output_boy.avi", fourcc, 20.0, (640,480))

width = str(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print(width)
height = str(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(height)
text = "Width:"+ width + " Height:" + height
font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        Time = str(datetime.datetime.now())
        frame = cv2.putText(frame, Time, (10,50), font, 1, (255,255,255), 2, cv2.LINE_AA)

        cv2.imshow("video playing rn ;)",frame)

        out.write(frame)

        if cv2.waitKey(1) == ord('t'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()