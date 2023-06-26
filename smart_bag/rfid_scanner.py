import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Set the serial port and baud rate to match your Arduino configuration
serial_port = 'COM3'  # Replace with the correct serial port
baud_rate = 9600  # Replace with the correct baud rate

# Create a serial connection
ser = serial.Serial(serial_port, baud_rate)

# Replace 'path/to/serviceAccountKey.json' with the path to your downloaded service account key
cred = credentials.Certificate('smartbag-c9652-firebase-adminsdk-7iapm-8034d7a790.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Specify the collection and document name
collection_name = 'scanned_data'
document_name = 'subject'

# Check if the document exists
doc_ref = db.collection(collection_name).document(document_name)
document = doc_ref.get()

if document.exists:
    # Document exists, delete the data
    scanned_data = document.to_dict()['data']
    scanned_data.pop()  # Remove the latest scanned item
else:
    # Document doesn't exist, create it with empty data
    scanned_data = []

while True:
    # Read a line of data from the serial monitor
    line = ser.readline().decode().strip()

    # Process and use the received data
    if line:
        print(f'Received data: {line}')

        # Add or remove data based on scanning
        if line == '41 B7 5C DF':
            data_to_add = 'physics'
        elif line == '41 9C 8F F0':
            data_to_add = 'chemistry'
        elif line == 'B1 23 E2 F0':
            data_to_add = 'maths'
        else:
            data_to_add = line

        if data_to_add not in scanned_data:
            print(f'Stored data: {data_to_add}')
            scanned_data.append(data_to_add)
        else:
            print(f'Removed data: {data_to_add}')
            scanned_data.remove(data_to_add)

        # Update the document in Firestore
        doc_ref.set({'data': scanned_data})

        # Break the loop if a specific condition is met
        if line == 'exit':
            break

# Close the serial connection
ser.close()

# Close the Firestore client
firebase_admin.delete_app(firebase_admin.get_app())

