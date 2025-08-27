📘 Facial Recognition Attendance System

A real-time facial recognition system that logs attendance by identifying known individuals through a webcam. Built using Python, OpenCV, and the face_recognition library.

📁 Folder Structure

Facial Detection/
├── attendance.py                  # Main script for running face recognition and logging attendance
├── Attendance.csv                 # Automatically generated attendance log
├── known_faces/                  # Folder containing subfolders for each registered person
│   ├── Aditya/                   # Subfolder named after the person
│   │   ├── aditya1.jpg           # Clear image of Aditya's face
│   ├── Priya/
│   │   └── priya1.jpg
│   └── ...                       # Add more people as needed
├── Dlib-Precompiled-Wheels/     # Folder containing downloaded .whl files for dlib
│   └── dlib-19.22.99-cp39-cp39-win_amd64.whl
└── README.md                     # This documentation file

⚙️ Setup Instructions

1. Clone or Download the Project

Place all files in a working directory, e.g., Facial Detection.

2. Install Required Packages

Use a virtual environment for clean setup:

python -m venv .venv
.\.venv\Scripts\activate
pip install opencv-python face_recognition pandas

3. Install dlib (Windows)

If installing dlib fails due to missing CMake, follow one of these:

✅ Recommended: Install CMake from cmake.org and add it to your system PATH.

🧪 Alternative: Use a precompiled .whl file from Unofficial Windows Binaries and install it:

pip install "path_to\dlib-19.22.99-cp39-cp39-win_amd64.whl"

4. Prepare Known Faces

Inside known_faces/, create folders named after each person and add clear face images.

🚀 How to Run

python attendance.py

The webcam will activate and begin scanning for known faces.

Attendance will be logged in Attendance.csv with timestamp.

Press q to quit the session.

🧠 Features

Real-time face recognition using face_recognition

Attendance logging with timestamp

Prevents duplicate entries per session

Easily expandable by adding new face folders

🧯 Troubleshooting

❌ Error: ModuleNotFoundError: No module named 'cmake'

This occurs when installing dlib without CMake installed. Fix by:

Installing CMake from cmake.org

Ensuring it's added to your system PATH

❌ Error: Could not find a version that satisfies the requirement cv2

You tried:

pip install cv2

Fix: Use the correct package name:

pip install opencv-python

❌ Error: .whl file not found

Make sure the path to your .whl file is correct and wrapped in quotes if it contains spaces:

pip install "C:\path\to\dlib-19.22.99-cp39-cp39-win_amd64.whl"

🙌 Credits

Developed by Aditya SrivastavaPowered by Python, OpenCV, and dlib

Also there is a problem facing during the uploading of the files in the GitHub as many folders are not able to upload properly, I tried to find the reason but it doesn't seems to be a proper solution. 
Also CV2 is not able to load instead all modules are perfectively installed. 
Don't know the actual reason. 
