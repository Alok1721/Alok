import cv2

# Read the input image
image = cv2.imread('shapes.png',0)

# Convert the image to grayscale


# Apply thresholding to the grayscale image
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Display the thresholded image
cv2.imshow('Thresholded Image', binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
