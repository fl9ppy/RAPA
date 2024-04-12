import cv2
import os

# Prompt user for name
name = input("Enter the name for the captured face: ")

# Create a folder to save the captured faces if it doesn't exist
save_folder = "captured_faces"
os.makedirs(save_folder, exist_ok=True)

# Initialize camera
cap = cv2.VideoCapture(0)

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_captured = False  # Flag to indicate if a face has been captured

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces and capture photo
    for (x, y, w, h) in faces:
        if not face_captured:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Capture the face and save it with the provided name
            face_img = frame[y:y+h, x:x+w]
            face_file = os.path.join(save_folder, f"{name}.jpg")
            cv2.imwrite(face_file, face_img)
            print("Face captured and saved.")
            face_captured = True

    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
