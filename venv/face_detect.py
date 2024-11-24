import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread("_DSC7467.jpg")
cap = cv2.VideoCapture("Megamind.avi")

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == ord('e'):
        break;

cap.release()
cv2.destroyAllWindows()