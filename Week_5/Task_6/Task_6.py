import cv2
import numpy as np
# Project 6: Augmented Reality Marker
# Goal: Final Project- Create AR by overlaying digital content on real-world markers.
# Your Challenge:
# Create a program that detects a special marker (like a colored paper or printed code) and
# places a virtual image/video on top of it.
# Step-by-step:
# 1. Detect your marker (using color or shape detection)
# 2. Find the marker's corners and perspective
# 3. Prepare your virtual content (image/logo)
# 4. Overlay the content perfectly onto the marker
# 5. Watch as digital content appears in your physical world!

cam_cappp = cv2.VideoCapture(0)
#fosforlu sarı için
lower_color = np.array([25, 150, 150])
upper_color = np.array([35, 255, 255])


logo = cv2.imread("github logo.png", cv2.IMREAD_UNCHANGED)
logo_height, logo_width = logo.shape[:2]

prev_pts = None
smooth_factor = 0.2

kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cam_cappp.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            epsilon = 0.02 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            if len(approx) == 4:
                pts_marker = np.float32([pt[0] for pt in approx])

                if prev_pts is None:
                    smooth_pts = pts_marker
                else:
                    smooth_pts = (1 - smooth_factor) * prev_pts + smooth_factor * pts_marker

                prev_pts = smooth_pts

                pts_logo = np.float32([[0, 0], [logo_width, 0], [logo_width, logo_height], [0, logo_height]])

                matrix = cv2.getPerspectiveTransform(pts_logo, smooth_pts)
                warped_logo = cv2.warpPerspective(logo, matrix, (frame.shape[1], frame.shape[0]))


                if logo.shape[2] == 4:
                    alpha = warped_logo[:, :, 3] / 255.0
                    for c in range(0, 3):
                        frame[:, :, c] = alpha * warped_logo[:, :, c] + (1 - alpha) * frame[:, :, c]
                else:
                    gray_logo = cv2.cvtColor(warped_logo, cv2.COLOR_BGR2GRAY)
                    _, mask_logo = cv2.threshold(gray_logo, 1, 255, cv2.THRESH_BINARY)
                    mask_inv = cv2.bitwise_not(mask_logo)
                    frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
                    logo_fg = cv2.bitwise_and(warped_logo, warped_logo, mask=mask_logo)
                    frame = cv2.add(frame_bg, logo_fg)


    cv2.imshow("Augmented Reality", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam_cappp.release()
cv2.destroyAllWindows()
