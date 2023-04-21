import cv2

# Load the image
img = cv2.imread('shapes.png',0)

# Convert the image to grayscale
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image
thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

# Find contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours
for cnt in contours:
    # Approximate the contour
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

    # Determine the shape of the contour based on the number of vertices
    num_vertices = len(approx)
    if num_vertices == 3:
        shape = "triangle"
    elif num_vertices == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)

        # Determine if the contour is a square or a rectangle based on the aspect ratio
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            shape = "square"
        else:
            shape = "rectangle"
    else:
        shape = "circle"

    # Draw the shape name on the image
    cv2.putText(img, shape, (cnt[0][0][0], cnt[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with shape names
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
