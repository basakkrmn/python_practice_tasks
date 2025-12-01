import cv2
import numpy as np

# Project 5: The Motion Tracker
# Goal: Detect movement and track objects as they move.
# Your Tasks:
# 1. Use background subtraction to highlight moving objects
# 2. Clean up the detection using erosion/dilation
# 3. Draw boxes around moving objects in real-time
# 4. Track the path of the largest moving object
# 5. Create a "security system" that alerts when something enters a defined zone
# Hint: Background subtractors can separate moving objects from static scenes.

video_capp = cv2.VideoCapture("hiking_man.mp4")
background_sub = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((5, 5), np.uint8)

zone_top_left = (100, 100)
zone_bottom_right = (400, 400)
path_points = []

while True:
    ret, frame = video_capp.read()
    if not ret:
        break


    frame_mask = background_sub.apply(frame)
    frame_mask = cv2.morphologyEx(frame_mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(frame_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if contours:
        largest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest)
        center = (x + w // 2, y + h // 2)

    if center is not None:
        path_points.append(center)

    cv2.rectangle(frame, zone_top_left, zone_bottom_right, (0, 0, 255), 2)

    if center is not None:
        if zone_top_left[0] < center[0] < zone_bottom_right[0] and zone_top_left[1] < center[1] < zone_bottom_right[1]:
            cv2.putText(frame, "ALERT!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    for i in range(1, len(path_points)):
        cv2.line(frame, path_points[i - 1], path_points[i], (255, 0, 0), 2)

    cv2.imshow("Motion Tracker", frame)
    cv2.imshow("Mask", frame_mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video_capp.release()
cv2.destroyAllWindows()
