📘 Facial Recognition Attendance System

Output of the project
<img width="636" height="514" alt="Image" src="https://github.com/user-attachments/assets/95201696-d9b2-41fe-bd8c-cf88d5050ef9" />

A real-time facial recognition–based attendance system that identifies known individuals via webcam and automatically records their attendance with timestamps.

Built using Python, OpenCV, face_recognition, and dlib.

**✨ Key Features**
Real-time face detection and recognition
Automatic attendance logging with date & time
Prevents duplicate entries during a session
Simple folder-based user management
CSV export for easy reporting
Easily extensible — just add new face images

**📁 Project Structure**
Facial Detection/
│
├── attendance.py                  # Main recognition & attendance script
├── Attendance.csv                # Auto-generated attendance file
│
├── known_faces/                  # Training images (one folder per person)
│   ├── Aditya/
│   │   └── aditya1.jpg
│   ├── Priya/
│   │   └── priya1.jpg
│   └── ...
│
├── Dlib-Precompiled-Wheels/
│   └── dlib-19.22.99-cp39-cp39-win_amd64.whl
│
└── README.md


Each subfolder inside known_faces represents one person.
Folder name = Person name.

**⚙️ Setup Instructions (Windows)**
1️⃣ Clone or Download
Extract the project into a directory such as:
Facial Detection

2️⃣ Create Virtual Environment (Recommended)
python -m venv .venv
.\.venv\Scripts\activate

3️⃣ Install Dependencies
pip install opencv-python face_recognition pandas

4️⃣ Install dlib
If pip install dlib fails:

**✅ Method 1 (Recommended)**
Install CMake from:
https://cmake.org/download/
During installation, check:

**✅ Add CMake to system PATH**
Then retry:
pip install dlib

**🧪 Method 2 (Precompiled Wheel)**
pip install "Dlib-Precompiled-Wheels\dlib-19.22.99-cp39-cp39-win_amd64.whl"


Make sure Python version matches (cp39 = Python 3.9).

📸 Preparing Known Faces

Inside known_faces/:

Create folders named after each person

Add clear front-facing images

One image is sufficient (more improves accuracy)

Example:

known_faces/Aditya/aditya1.jpg

🚀 Running the Project
python attendance.py

**Behavior:**
Webcam opens
Faces are recognized
Attendance written to Attendance.csv
Press Q to exit

**📄 Attendance Output**
CSV format:
Name, Time
Aditya, 10:23:41
Priya, 10:24:05

GitHub does NOT upload empty folders.

If your directories contain no files, they will silently disappear.

✅ Fix
Add a placeholder file:
known_faces/.gitkeep
or
touch known_faces/.gitkeep
Then commit again.
Also avoid uploading:
.venv
.csv
.whl
Add .gitignore:

.venv/
Attendance.csv
*.whl

❌ cv2 Not Found
Cause
You installed:
pip install cv2
❌ WRONG

✅ Fix
pip uninstall cv2
pip install opencv-python


**Verify:**
python -c "import cv2; print(cv2.__version__)"
❌ dlib / cmake Error
Error:
ModuleNotFoundError: No module named 'cmake'

**Fix:**
Install CMake + add to PATH, or use precompiled .whl.
❌ cv2 Installed But Still Not Loading

**Most common causes:**
Multiple Python Versions
Check:
where python
where pip
They MUST point to same environment.

🔮 Future Enhancements (Optional)
Excel export
Database storage
GUI interface
Mask detection
Multi-camera support
Cloud sync

🙌 Credits
Developed by Aditya Srivastava
Powered by:
Python
OpenCV
face_recognition
dlib
