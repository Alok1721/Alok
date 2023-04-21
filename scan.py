import cv2
from pyzbar import pyzbar

# Define the colors to be detected in the HSV color space
colors = {'red': ([0, 100, 100], [10, 255, 255]), 'green': ([36, 25, 25], [86, 255, 255]), 'blue': ([100, 50, 50], [130, 255, 255])}

# Start the video capture
cap = cv2.VideoCapture('barcode.mp4')

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Loop over the defined colors
    for color, (lower, upper) in colors.items():
        # Threshold the image to extract the color of interest
        mask = cv2.inRange(hsv, lower, upper)

        # Find the contours of the thresholded image
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Loop over the contours to identify the shape
        for contour in contours:
            # Approximate the contour to reduce the number of vertices
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

            # Identify the shape based on the number of vertices
            shape = None
            if len(approx) == 3:
                shape = "triangle"
            elif len(approx) == 4:
                shape = "rectangle"
            elif len(approx) == 5:
                shape = "pentagon"
            elif len(approx) == 6:
                shape = "hexagon"
            elif len(approx) > 6:
                shape = "circle"

            # Print the shape and color on the terminal
            if shape:
                print(f"Detected {color} {shape}")

    # Display the original frame
    cv2.imshow('frame', frame)

    # Check if the user pressed the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
