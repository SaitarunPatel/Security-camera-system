import cv2
import datetime as dt

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output_boy.avi", fourcc, 24, (640, 480))
font = cv2.FONT_HERSHEY_SIMPLEX

#calculating the Total number of Pixels captured by the camera.
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_pixels = width * height

#Checking if the camera is returning frame
try:
    master_ret, master_image = cap.read()
    master_image = cv2.GaussianBlur(master_image, (5, 5), 0)
    master_image = cv2.medianBlur(master_image, 5)
    master_image = cv2.bilateralFilter(master_image, 9, 75, 75)
except:
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    exit(0)

#Master_image is selected and now all other frames read by camera is compared with it.
while cap.isOpened():
    ret, frame = cap.read()
    time = str(dt.datetime.now())
    if ret == True:
        #Displaying the Current frame
        cv2.imshow("Camera feed", frame)
        # master_blurred = cv2.GaussianBlur(master_image, (5, 5), 0)
        frame_filtered = cv2.GaussianBlur(frame, (5, 5), 0)
        frame_filtered = cv2.medianBlur(frame_filtered, 5)
        frame_filtered = cv2.bilateralFilter(frame_filtered, 9, 75, 75)
        # Calculating difference in Master frame and current frame
        difference_in_master_frame = cv2.subtract(master_image, frame_filtered)
        #Calculating difference if Master frame and current frame
        # difference_in_master_frame = cv2.subtract(master_image, frame)
        #Displaying the differnce
        cv2.imshow("Difference", difference_in_master_frame)
        #Splitting the Difference in BGR
        b, g, r = cv2.split(difference_in_master_frame)
        #Counting the number of NON-ZERO values in B, G, R frames
        blue_count = cv2.countNonZero(b)
        green_count = cv2.countNonZero(g)
        red_count = cv2.countNonZero(r)
        #Calculating Average NON-ZERO values from B, G, R frames
        average_frame_non_zero_count = int((blue_count+green_count+red_count)/3)
        #Calculating the Percent Difference
        percent_difference = float(average_frame_non_zero_count/total_pixels)
        print(percent_difference)
        #If there is a differnce greater than 15% in the Current frame and the Master frame, the current frame is
        #is stored in output file.
        if percent_difference > 0.5:
            #Adding Time-stamp to the frame before storing it
            frame = cv2.putText(frame, time, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            out.write(frame)

        #Condition for breaking out of the while loop without disconnecting the camera
        if cv2.waitKey(1) == ord('e'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
exit(0)