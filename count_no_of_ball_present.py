import cv2

# Read the input image
image = cv2.imread("balls.jpg",0)

# Convert the image to grayscale
#gray = cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)

gray=image
# Apply a threshold to the image to convert it to binary
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(image, contours, -1, (0, 0, 255), 2)

# Count the number of contours (balls) in the image
count = len(contours)

# Write the count on the image
cv2.putText(image, f"Count: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Save the output image
#cv2.imwrite("count.png", image)

# Display the output image
#cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
