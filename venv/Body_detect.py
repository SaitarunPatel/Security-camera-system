import cv2

#body_detect = cv2.CascadeClassifier("haarcascade_fullbody.xml")
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread("70528878490932144561.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
body = face_detect.detectMultiScale(gray, 1.1, 4)

for (x, y ,w , h) in body:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

cv2.imshow("Deetcg???", img)

if cv2.waitKey(0) == ord('e'):
    cv2.destroyAllWindows()