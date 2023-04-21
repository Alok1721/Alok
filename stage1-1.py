import cv2
import numpy as np

# Define the colors to detect
colors_to_detect = {
    "red": ((0, 50, 50), (10, 255, 255)),
    "blue": ((110, 50, 50), (130, 255, 255)),
    "green": ((50, 100, 100), (70, 255, 255))
}

# Define the minimum and maximum areas for each shape
shape_min_areas = {
    "circle": 100,
    "square": 200,
    "triangle": 200
}

# Define the shape detection function
def detect_shape(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    num_sides = len(approx)

    if num_sides == 3:
        return "triangle"
    elif num_sides == 4:
        x,y,w,h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        if 0.95 <= aspect_ratio <= 1.05:
            return "square"
        else:
            return "rectangle"
    else:
        return "circle"

# Open the video source
cap = cv2.VideoCapture('shapes.mp4')

# Loop through the frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect the colors of the shapes
    for color_name, color_range in colors_to_detect.items():
        mask = cv2.inRange(hsv, color_range[0], color_range[1])
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Loop through the contours
        for contour in contours:
            area = cv2.contourArea(contour)

            # Only process contours that meet the minimum area requirement
            if area >= shape_min_areas["circle"]:
                shape_name = detect_shape(contour)

                # Draw a bounding box around the shape and print its color and shape
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"{color_name} {shape_name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(f"Detected {color_name} {shape_name}")

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for a key press and check if it's the escape key
    if cv2.waitKey(1) == 27:
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
