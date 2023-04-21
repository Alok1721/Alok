import cv2

# Load image
img = cv2.imread('shapes.png',0)

# Convert to grayscale
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Display the result
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
