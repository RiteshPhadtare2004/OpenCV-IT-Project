import cv2

# Use cv2.VideoCapture with CAP_DSHOW backend
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale frames
    cv2.imshow('Original', frame)
    cv2.imshow('Grayscale', gray)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
