import cv2
import face_recognition
import os

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load known faces and their names
known_faces_folder = "captured_faces"
known_face_encodings = []
known_face_names = []

# Load known faces and their encodings
for file_name in os.listdir(known_faces_folder):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        name = os.path.splitext(file_name)[0]
        image = face_recognition.load_image_file(os.path.join(known_faces_folder, file_name))
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(name)

# Initialize camera
cap = cv2.VideoCapture(0)

# Adjust camera properties for smoother feed
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)

while True:
    # Read frame from camera
    ret, frame = cap.read()
    
    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Convert frame to RGB for face_recognition library
    rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    # Draw rectangles around the faces and recognize them
    for (x, y, w, h), face_encoding in zip(faces, face_encodings):
        # Compare the face encoding with the known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        for i, match in enumerate(matches):
            if match:
                name = known_face_names[i]
                break
        
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x*4, y*4), ((x+w)*4, (y+h)*4), (255, 0, 0), 2)
        
        # Draw a label with the name below the face
        cv2.putText(frame, name, (x*4, (y+h)*4+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
