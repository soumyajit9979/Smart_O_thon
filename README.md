SMART SCHOOLING
21BAI1118-RAGHUVIR SINGH SENGAR
21BRS1608-SOUMYAJIT SEN SHARMA
21BRS1643- OMKAR ADITYA SAHOO


OUR PROJECT:
WE HAVE THREE OBJECTIVES COVERED IN OUR PROJECT:

1.	SMART BAG
2.	SMART ATTENDANCE TRACKER
3.	TEXT TO SPEECH
SMART  BAG

https://user-images.githubusercontent.com/82709454/248779414-6be860a9-26c8-41a9-9d9e-13c9287a8c44.mp4

1.	WE HAVE CREATED A WEBSITE AND A WORKING MODEL USING ARDUINO AND RFID and ALSO DATA IS STORED IN FIRESTORE DATABASE , TWILLO LIBRARY

   ![IMG-20230626-WA0019](https://github.com/soumyajit9979/Smart_O_thon/assets/82709454/aee87063-3255-4ffd-94b7-8b67d2d7456c)
   

    https://user-images.githubusercontent.com/82709454/248779293-1a8e03d4-f593-4cef-ab28-514c795f4c2f.jpg

   
a. THE WEBSITE HELPS IN CREATING A TIMETABLE FOR THE STUDENTS
b. THE WORKING MODEL HAS THE FOLLOWING FEATURES:

1.	WE HAVE ASSUMED THAT RFID CHIPS WILL BE FITTED ON COPIES
2.	NOW ACCORDING TO TIMETABLE (LETS ASSUME MONDAY), THERE IS REQUIREMENT OF 3 SUBJECT COPIES: MATHS, PHYSICS AND CHEMISTRY
3.	WE WILL HAVE A RFID SCANNER ON THE ENTRANCE OF THE BAG
4.	WHEN WE PUT A COPY INSIDE THE BAG, THE SCANNER SCANS THE COPY AND ENTERS (FOR EXAMPLE MATHS) INTO THE DATABASE.
   https://user-images.githubusercontent.com/82709454/248779306-ed31705f-d777-45cb-9a60-077bc6831467.jpg
  	
6.	WHEN WE TAKE OUT THE MATH COPY THEN RFID ON THE MATH COPY IS SCANNED AGAIN AND THE MATH RECORD IS AUTOMATICALLY DELETED FROM THE DATABASE
7.	NOW LIKE THAT WE PUT MATH AND CHEMISTRY COPY IN BAG.
8.	NOW ON RUNNING THE COMPARISION CODE, IT CHECKS WHICH WHAT COPIES ARE MISSING FROM MONDAYS TIMETABLE AND WHAT COPIES ARE EXTRA
9.	FOR EG. IN MONDAYS TIMETABLE THERE IS PHYSICS,CHEMISTRY AND MATH. THEN IF WE PUT MATH, CHEM, BIOLOGY COPY IN BAG, THEN RFID WILL BE SCANNED AND ADDED IN DATABASE
   https://user-images.githubusercontent.com/82709454/248779299-f9f7e127-e372-4e41-9ff7-a64ba4d3cf70.jpg
10.	ALSO MESSAGE WILL COME TO OUR PHONE THAT WE ARE MISSING PHYISCS COPY FROM BAG AND BIOLOGY COPY IS EXTRA. 
THIS HELPS IN TELLING WHAT COPIES THE STUDENT IS MISSING AND WHAT EXTRA COPIES THE STUDENT IS CARRYING

https://user-images.githubusercontent.com/82709454/248779071-e6ee03cb-3f7e-4f5d-afc7-826cabfa8d1d.jpg



SMART ATTENDANCE TRACKER
The project you described is an attendance system that utilizes an Arduino and a fingerprint sensor to store attendance data of present students in Excel as well as Firebase. Here's a detailed explanation of how this project works:

Arduino: The Arduino serves as the microcontroller in this project, responsible for controlling the fingerprint sensor and managing the attendance data.

Fingerprint Sensor: The fingerprint sensor is used to capture the unique fingerprint of each student. It can authenticate and match the fingerprint to the stored fingerprint templates.

Attendance Data Storage: The attendance data is stored in two locations: Excel and Firebase.

a. Excel: The Arduino is connected to a computer where Microsoft Excel is installed. The Arduino utilizes libraries or software to establish a connection with Excel and writes the attendance data to a specific Excel sheet or CSV file. Each student's attendance is recorded with a timestamp, marking their presence.

b. Firebase: Firebase is a cloud-based platform provided by Google for storing and managing data. The Arduino communicates with the Firebase Realtime Database or Firestore to store attendance data. The attendance data can be structured using collections and documents, with each student having a unique document containing their attendance records.

Fingerprint Enrollment: Before recording attendance, the fingerprint sensor needs to enroll the fingerprints of all the students in the system. Each student's fingerprint is captured and stored as a template in the Arduino's memory or external storage.

Attendance Recording: When a teacher wants to take attendance, they initiate the process by interacting with the Arduino. The Arduino prompts the teacher to place their finger on the fingerprint sensor for authentication. Once the teacher's fingerprint is verified, the attendance session begins.

Student Attendance: Students place their fingers on the fingerprint sensor one by one. The fingerprint sensor captures and matches the fingerprints with the stored templates. If a match is found, it indicates that the student is present, and the attendance is recorded.

Locking Attendance: After the attendance session, the teacher locks the attendance to prevent further modifications. This action can be performed through an input mechanism, such as a button or keypad connected to the Arduino. Once locked, the attendance data is considered final and cannot be changed.

Data Storage and Sync: The Arduino then writes the attendance data to the Excel sheet or CSV file on the connected computer. Additionally, it communicates with the Firebase platform to store the attendance data in the designated database.

Data Accessibility: The attendance data can be accessed later for reporting or analysis purposes. The Excel sheet or CSV file can be opened and analyzed using spreadsheet software, while the attendance data in Firebase can be accessed and queried programmatically using the Firebase API.

In summary, this project combines an Arduino, a fingerprint sensor, and data storage mechanisms (Excel and Firebase) to create an attendance system. The fingerprint sensor is used for identification, the Arduino manages the attendance process and data storage, and attendance records are stored in both Excel and Firebase for accessibility and analysis.
TEXT TO SPEECH
Our next project aims to assist blind individuals in reading by converting text captured from a video feed into speech. It utilizes a Raspberry Pi and a webcam as the main components. Here's a detailed explanation of how this project works:

1. Raspberry Pi: The Raspberry Pi is a small, affordable computer board that can be used for various projects. In this case, it serves as the main processing unit for the text-to-speech conversion system. The Raspberry Pi runs the necessary software and controls the webcam for capturing the video feed.

2. Webcam: A webcam is used to capture the video that contains the text to be read. The webcam should be connected to the Raspberry Pi, and its feed is processed to extract the text information.

3. Video Processing: The video feed captured by the webcam is processed to identify and extract the text present within the frames. Optical Character Recognition (OCR) techniques are commonly used for this purpose. OCR algorithms analyze the video frames, detect text regions, and convert them into digital text.

4. Text-to-Speech Conversion: Once the text is extracted from the video frames, the Raspberry Pi uses a text-to-speech synthesis engine to convert the text into audible speech. There are several text-to-speech libraries available for the Raspberry Pi, such as eSpeak or Google Text-to-Speech.

5. Speech Output: The Raspberry Pi plays the synthesized speech output through a speaker or headphones connected to its audio output. The blind person can hear the words spoken aloud, allowing them to comprehend the text content.

6. User Interface: The project may include a user interface for the blind person to interact with the system. This interface could involve physical buttons or a tactile keypad for controlling the text capture and speech playback. The Raspberry Pi can process these inputs and perform the necessary actions, such as capturing video or adjusting the speech settings.

7. Accessibility Features: To enhance accessibility, the system can incorporate additional features like voice-controlled commands or audio feedback for user interactions. These features can further assist blind individuals in navigating and utilizing the system effectively.

Overall, this project combines the capabilities of a Raspberry Pi and a webcam to capture video containing text, perform OCR to extract the text, convert it to speech using a text-to-speech synthesis engine, and provide audible output for blind individuals. It offers a practical solution to help visually impaired individuals read and access textual information more independently.
