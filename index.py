import cv2
import numpy as np

# Load the image
img = cv2.imread('shapes.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray_blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Detect circles using the Hough Circle Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50,
                           param1=100, param2=30, minRadius=0, maxRadius=0)

# Draw detected circles on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)

# Find contours of the shapes
_, contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the detected shapes
for cnt in contours:
    # Approximate the contour to a polygon
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

    # If the polygon has 3 vertices, it's a triangle
    if len(approx) == 3:
        cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)

    # If the polygon has 4 vertices, it's a square
    elif len(approx) == 4:
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

# Display the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
