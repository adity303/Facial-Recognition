import cv2
import pandas as pd
from datetime import datetime
import os

# Personal details
user_name = "Aditya Srivastava"
user_age = 22

# Attendance file setup
attendance_file = "Attendance.csv"
if os.path.exists(attendance_file):
    df = pd.read_csv(attendance_file)
else:
    df = pd.DataFrame(columns=["Name", "Age", "Time"])

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture
cap = cv2.VideoCapture(0)
logged_faces = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Simulate identity using hash of face region
        face_region = gray[y:y+h, x:x+w]
        face_id = hash(face_region.tobytes()) % 10000

        if face_id not in logged_faces:
            # Log attendance
            timestamp = datetime.now().strftime("%H:%M:%S")
            df.loc[len(df)] = [user_name, user_age, timestamp]
            df.to_csv(attendance_file, index=False)
            logged_faces.append(face_id)

        # Display name and age
        label = f"{user_name}, Age: {user_age}"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Face Attendance System", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

