# Python Practice Tasks – Week 5
This folder contains my Python exercises for Week 5. Each project focuses on computer vision concepts, helping me improve problem-solving skills and Python knowledge using OpenCV and NumPy.

## What You'll Need
Install the required Python packages:

```bash
pip install opencv-python numpy
```
## Projects Included
**Project 1: The Digital Darkroom (Image Manipulation)**

**Goal:** Learn to load, display, and transform images like a photo editor.

**Tasks:**

1.Load an image and display it in a window.

2.Print the image's dimensions and color channels.

3.Split the image into Blue, Green, and Red layers and display each separately.

4.Create a "channel-swapped" version (swap Red and Blue).

5.Crop and resize the image.

6.Convert to grayscale and create custom filters (warm tones, vintage look).

**Demonstrates:** Image loading, displaying, NumPy array manipulations, and color channel operations.

**Project 2: The Video Wizard (Video Processing)**

**Goal:** Work with live video and create interactive drawings.

**Tasks:**

1.Access your webcam and display the live feed.

2.Play a video file from your computer.

3.Draw shapes (rectangles, circles) and text on the video.

4.Create a simple "paint" program that draws where you click.

5.Add a screenshot feature (save a frame when you press 's').

**Demonstrates:** Video capture and processing frame by frame, mouse events, drawing, and text overlay.

**Project 3: The Shape & Color Detective (Object Detection)**

**Goal:** Make your program detect objects by color and shape.

**Tasks:**

1.Track a colored object using HSV color space.

2.Find and draw contours around detected objects.

3.Filter out small or noisy detections.

4.Draw bounding boxes around the largest detected object.

5.Bonus: Detect specific shapes (squares, circles, triangles).

**Demonstrates:** Color detection, contour detection, and filtering with OpenCV.

**Project 4: The Smart Selfie App (Face Detection & Filters)**

**Goal:** Create fun face filters and effects using face detection.

**Tasks:**

1.Detect faces in images using Haar Cascades.

2.Implement real-time face detection on webcam.

3.Add a "privacy blur" over detected faces.

4.Create a virtual glasses filter that sticks to faces.

5.Count and display how many faces are in view.

**Demonstrates:** Real-time face detection, Haar Cascades, image overlay, and face tracking.

**Project 5: The Motion Tracker (Movement Tracking)**

**Goal:** Detect movement and track objects as they move.

**Tasks:**

1.Use background subtraction to highlight moving objects.

2.Clean up the detection using erosion/dilation.

3.Draw boxes around moving objects in real-time.

4.Track the path of the largest moving object.

5.Create a "security system" that alerts when something enters a defined zone.

**Demonstrates:** Motion detection, contour analysis, object tracking, and simple alert systems.

**Project 6: Augmented Reality Marker (AR Overlay)**

**Goal:** Final Project – Create AR by overlaying digital content on real-world markers.

**Challenge:** Detect a special marker and place a virtual image/video on top of it.

**Tasks:**

1.Detect your marker (using color or shape detection).

2.Find the marker's corners and perspective.

3.Prepare your virtual content (image/logo).

4.Overlay the content perfectly onto the marker.

5.Watch as digital content appears in your physical world.

**Demonstrates:** Color detection, perspective transformation, image overlay, and augmented reality basics.

## How to Run

- Each project is independent.

- Open the Python file for each project and run it in your preferred environment (PyCharm, VS Code, etc.).

- Follow on-screen prompts for input where applicable.