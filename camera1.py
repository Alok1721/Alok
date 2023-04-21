import cv2

# Open the video file
cap = cv2.VideoCapture('vid.mp4')

# Loop through the frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read  
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for a key press and check if it's the escape key
    if cv2.waitKey(1) == 27:
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
