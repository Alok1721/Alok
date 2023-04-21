import cv2

# Define the tracker type
tracker_type = 'MIL'

# Initialize the tracker
if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
elif tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
elif tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
elif tracker_type == 'MOSSE':
    tracker = cv2.TrackerMOSSE_create()
elif tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

# Open the video file
cap = cv2.VideoCapture('vid.mp4')

# Read the first frame
ret, frame = cap.read()

# Select the region of interest (ROI)
roi = cv2.selectROI(frame, False)

# Initialize the tracker with the ROI and the first frame
tracker.init(frame, roi)

# Loop through the frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Update the tracker with the new frame
    success, roi = tracker.update(frame)

    # If tracking is successful, draw a rectangle around the tracked object
    if success:
        (x, y, w, h) = [int(i) for i in roi]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for a key press and check if it's the escape key
    if cv2.waitKey(1) == 27:
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
