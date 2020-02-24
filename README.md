# Face_rec_ard
Using face_recognition to turn arduino on-board LED on and off based on the known and unknown person.

# Requirements

- Arduino Uno (I've used Arduino UNO R3)
- Arduino IDE
- Python (any version)
- Visual Studio Desktop Development Tools
- cMake

## Python Modules
- OpenCV
- Dlib (need to have cMake installed to install ***dlib***)
- Face_recognition
- PySerial

# How to use

- Clone the repository
- Upload **Helloworld.ino** to arduino board
- Change Serial name in **face_rec_live** under:
  **ArduinoConn = serial.Serial("change here", 9600)**
- Run **face_rec_live**
