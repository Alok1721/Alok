import cv2
import numpy as np

# Load the image
img = cv2.imread('triangle.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 100, 200)

# Detect lines using Hough transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# Draw lines on the image
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Show the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
