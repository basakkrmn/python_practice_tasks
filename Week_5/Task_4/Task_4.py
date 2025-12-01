import cv2
import numpy as np

#  Project 4: The Smart Selfie App
#  Goal: Create fun face filters and effects using face detection.
#  Tasks:
#  1. Detect faces in images using Haar Cascades
#  2. Implement real-time face detection on webcam
#  3. Add a "privacy blur" over detected faces
#  4. Create a virtual glasses filter that sticks to faces
#  5. Count and display how many faces are in view

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
glasses = cv2.imread("glasses1.png", cv2.IMREAD_UNCHANGED)

cam_capp = cv2.VideoCapture(0)

while True:
    ret, frame = cam_capp.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:

        roi = frame[y:y + h, x:x + w]
        blur = cv2.GaussianBlur(roi, (25, 25), 0)
        frame[y:y + h, x:x + w] = blur


        glasses_width = w
        glasses_height = int(glasses.shape[0] * (glasses_width / glasses.shape[1]))

        y1 = y + int(h * 0.25)
        x1 = x


        if y1 + glasses_height > frame.shape[0]:
            glasses_height = frame.shape[0] - y1
        if x1 + glasses_width > frame.shape[1]:
            glasses_width = frame.shape[1] - x1

        resized_glasses = cv2.resize(glasses, (glasses_width, glasses_height))


        if resized_glasses.shape[2] == 4:
            alpha_glasses = resized_glasses[:, :, 3] / 255.0
        else:
            alpha_glasses = np.ones((glasses_height, glasses_width))


        for c in range(0, 3):
            frame[y1:y1 + glasses_height, x1:x1 + glasses_width, c] = (
                alpha_glasses * resized_glasses[:, :, c] +
                (1 - alpha_glasses) * frame[y1:y1 + glasses_height, x1:x1 + glasses_width, c]
            )


    cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam_capp.release()
cv2.destroyAllWindows()
