from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate(
    "smartbag-c9652-firebase-adminsdk-7iapm-8034d7a790.json"
)
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/", methods=["GET", "POST"])
def create_timetable():
    if request.method == "POST":
        studentID = request.form["studentID"]
        day = request.form["day"]
        numbers = request.form["numbers"]
        items = []
        number = int(numbers)
        for i in range(number):
            j = str(i)
            subject = request.form["subject" + j]
            items.append(subject)

        # Create a timetable dictionary
        timetable = {"subject": items}

        # Add the timetable to Firestore
        timetable_ref = db.collection(studentID).document(day)
        timetable_ref.set(timetable)

        return "Timetable created and stored in Firestore."
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
