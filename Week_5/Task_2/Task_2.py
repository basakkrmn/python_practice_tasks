import cv2
import numpy as np
drawing = False
paint_color = (0, 0, 255)
brush_size = 5
# Project 2: The Video Wizard
#  Goal: Work with live video and create interactive drawings.
#  Your Tasks:
#  1. Access your webcam and display the live feed
#  2. Play a video file from your computer
#  3. Draw shapes (rectangles, circles) and text on the video
#  4. Create a simple "paint" program that draws where you click
#  5. Add a screenshot feature (save frame when you press 's')
# Hint: Use `cv2.VideoCapture(0)` for webcam. The key to video is processing frame by frame in
#  a loop.
def draw(event, x, y, flags, param):
    global drawing
    canvas = param
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(canvas, (x, y), brush_size, paint_color, -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(canvas, (x, y), brush_size, paint_color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cam_cap = cv2.VideoCapture(0)
ret, temp_frame = cam_cap.read()
canvas_webcam = np.zeros_like(temp_frame)

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", draw, canvas_webcam)

while True:
    ret, frame = cam_cap.read()
    if not ret:
        break


    frame = cv2.addWeighted(frame, 1, canvas_webcam, 1, 0)


    cv2.rectangle(frame, (50,50), (200,200), (0,255,0), 2)
    cv2.circle(frame, (300,300), 50, (255,0,0), 3)
    cv2.putText(frame, "Webcam Feed", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("webcam_screenshot.png", frame)
        print("Webcam screenshot alındı!")

cam_cap.release()
cv2.destroyAllWindows()

video_cap = cv2.VideoCapture("hogwarts_express.mp4")
ret, temp_frame = video_cap.read()
canvas_video = np.zeros_like(temp_frame)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", draw, canvas_video)

while True:
    ret, frame = video_cap.read()
    if not ret:
        break


    cv2.rectangle(frame, (50,50), (200,200), (0,255,0), 2)
    cv2.circle(frame, (300,300), 50, (255,0,0), 3)
    cv2.putText(frame, "Harry Potter", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


    frame = cv2.addWeighted(frame, 1, canvas_video, 1, 0)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("video_screenshot.png", frame)
        print("Video screenshot alındı!")

video_cap.release()
cv2.destroyAllWindows()


