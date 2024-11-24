import cv2

img1 = cv2.imread("lena.jpg")
img2 = cv2.imread("lena.jpg")

height = int(img1.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(img1.get(cv2.CAP_PROP_FRAME_WIDTH))
total = height * width
print(total)

dif = cv2.subtract(img1, img2)

cv2.imshow("DST", dif)

cv2.waitKey(0)