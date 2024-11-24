import cv2

img1 = cv2.imread("lena.jpg",0)
cv2.imshow("Test img display:",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()