import cv2
import numpy as np

# Project 3: The Shape & Color Detective
#  Goal: Make your program detect objects by color and shape.
#  Your Tasks:
#  1. Track a colored object (like a bright pen) using HSV color space
#  2. Find and draw contours around detected objects
#  3. Filter out small/noisy detections
#  4. Draw bounding boxes around the largest detected object
#  5. Bonus: Detect specific shapes (squares, circles, triangles)
#  Key Tools: `cv2.inRange()`, `cv2.findContours()`, and contour area filtering

lower_color = np.array([0, 120, 70])
upper_color = np.array([10, 255, 255])


video_path = "shapes.mp4"
video_cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = video_cap.read()
    if not ret:
        break


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, lower_color, upper_color)


    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)


    if contours:
        largest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)


        approx = cv2.approxPolyDP(largest, 0.04*cv2.arcLength(largest, True), True)
        shape = ""
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            shape = "Square/Rectangle"
        elif len(approx) > 8:
            shape = "Circle"
        if shape:
            cv2.putText(frame, shape, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)


    cv2.imshow("Shape & Color Detective", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()

