#applying the threshold for different value of pixel
import cv2

# Read the input image
image = cv2.imread('shapes.png',0)

# Convert the image to grayscale
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding with different threshold values
_, binary_image_50 = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
_, binary_image_100 = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
_, binary_image_200 = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

# Display the thresholded images
cv2.imshow('Binary Image 50', binary_image_50)
cv2.imshow('Binary Image 100', binary_image_100)
cv2.imshow('Binary Image 200', binary_image_200)

cv2.waitKey(0)
cv2.destroyAllWindows()
