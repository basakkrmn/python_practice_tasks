import cv2
import numpy as np
# Project 1: The Digital Darkroom
#  Goal: Learn to load, display, and transform images like a photo editor.
#  Your Tasks:
#  1. Load an image and display it in a window
#  2. Print the image's dimensions and color channels
#  3. Split the image into Blue, Green, and Red layers- display each separately
#  4. Create a "channel-swapped" version (swap Red and Blue)
#  5. Crop and resize the image
#  6. Convert to grayscale and create custom filters (warm tones, vintage look)
#  Hint: Remember `cv2.imread()`, `cv2.imshow()`, and that images are just NumPy arrays.


my_image = cv2.imread("colorful_landscape.webp")
cv2.imshow("Original Image",my_image)
cv2.waitKey(0)

print("Image shape:",my_image.shape)

blue,green,red= cv2.split(my_image)

cv2.imshow("Blue Channel",blue)
cv2.imshow("Green Channel",green)
cv2.imshow("Red Channel",red)

channel_swapped =cv2.merge([red,green,blue])
cv2.imshow("Red -Blue Swapped Image",channel_swapped)
cv2.waitKey(0)

cropped_img = my_image[50:300, 50:300]
resized_img = cv2.resize(cropped_img, (200, 200))
cv2.imshow("Cropped & Resized", resized_img)
cv2.waitKey(0)

gray_img= cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray_img)
cv2.waitKey(0)

warm_img = my_image.copy()
warm_img[:, :, 2] = cv2.add(warm_img[:, :, 2], 50)
warm_img[:, :, 0] = cv2.subtract(warm_img[:, :, 0], 30)
cv2.imshow("Warm Filter", warm_img)
cv2.waitKey(0)

vintage_img = cv2.GaussianBlur(my_image, (21, 21), 0)
vintage_img = cv2.addWeighted(my_image, 0.6, vintage_img, 0.4, 0)
cv2.imshow("Vintage Filter", vintage_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
