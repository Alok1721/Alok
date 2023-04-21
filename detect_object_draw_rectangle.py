import cv2

# Load the image
img = cv2.imread('shapes.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the grayscale image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Define the dictionary of shape names
shape_names = {
    3: "Triangle",
    4: "Rectangle",
    5: "Pentagon",
    6: "Hexagon"
}

# Loop through the contours and detect the shape
for cnt in contours:
    # Approximate the contour to a polygon
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)

    # Get the number of sides of the polygon
    sides = len(approx)

    # Only process polygons with 3, 4, 5, or 6 sides
    if sides in shape_names:
        # Draw a bounding box around the shape
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Put the name of the shape above the bounding box
        cv2.putText(img, shape_names[sides], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with bounding boxes and shape names
cv2.imshow('Math Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
