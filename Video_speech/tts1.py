import cv2
import pytesseract
import pyttsx3

# Webcam video device index
video_path = 0

# Load the video
cap = cv2.VideoCapture(video_path)

# Initialize variables
frame_count = 0
text = ''

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Read frames from the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform text extraction using pytesseract
    text = pytesseract.image_to_string(gray)

    frame_count += 1

    # Speak the extracted text
    engine.say(text)
    engine.runAndWait()

# Release the video capture object
cap.release()
