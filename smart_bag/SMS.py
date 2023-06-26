from twilio.rest import Client
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Twilio credentials
account_sid = "AC6b4eb901e1a001899b26646910090c57"
auth_token = "e6bfcdcb89f9b7d6b09856bdcd801b7f"
twilio_phone_number = "+14846421339"
recipient_phone_number = "+919978619693"

# Initialize Firebase app
cred = credentials.Certificate('smartbag-c9652-firebase-adminsdk-7iapm-8034d7a790.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Specify the paths to the documents
document_path_1 = 'scanned_data/subject'  # Replace with the actual path to the first document
document_path_2 = 'student1/monday'  # Replace with the actual path to the second document

# Retrieve the arrays from the first document
doc_ref_1 = db.document(document_path_1)
doc_1 = doc_ref_1.get()

if doc_1.exists:
    array1 = doc_1.to_dict().get('data')
else:
    print(f"Document {document_path_1} does not exist.")
    array1 = None

# Retrieve the arrays from the second document
doc_ref_2 = db.document(document_path_2)
doc_2 = doc_ref_2.get()

if doc_2.exists:
    array2 = doc_2.to_dict().get('data')
else:
    print(f"Document {document_path_2} does not exist.")
    array2 = None

# Compare the arrays bidirectionally
missing_elements = set(array2) - set(array1)

extra_elements = set(array1) - set(array2)

if missing_elements:
    for element in missing_elements:
        message = f"{element} is not in bag"
        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Send the SMS message
        sms_message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )

        print("SMS sent with SID:", sms_message.sid)

if extra_elements:
    for element in extra_elements:
        message = f"{element} is an extra item in the bag"
        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Send the SMS message
        sms_message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )

        print("SMS sent with SID:", sms_message.sid)

if not missing_elements and not extra_elements:
    print("Arrays are equal (irrespective of order). No missing or extra elements.")

# Clean up Firebase app
firebase_admin.delete_app(firebase_admin.get_app())
