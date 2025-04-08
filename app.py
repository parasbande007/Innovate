from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import random
import string

app = Flask(__name__)
CORS(app)

# MongoDB setup (you can update to your Atlas URI here)
client = MongoClient("mongodb://localhost:27017/")
db = client["fisglobal"]
tickets = db["requests"]

# Generate a random ticket number
def generate_ticket_number():
    return 'TKT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit_form():
    data = request.get_json()
    try:
        ticket_number = generate_ticket_number()
        data['ticketNumber'] = ticket_number
        data['status'] = 'Active'
        data['submittedAt'] = datetime.utcnow()

        tickets.insert_one(data)

        return jsonify({
            "message": "Form data saved successfully",
            "ticketNumber": ticket_number
        }), 200
    except Exception as e:
        return jsonify({
            "message": "Error saving form data",
            "error": str(e)
        }), 500

# API to get all tickets in JSON format
@app.route("/tickets")
def get_tickets():
    all_tickets = list(tickets.find({}, {'_id': 0}))  # Exclude MongoDB _id
    return jsonify(all_tickets)

# Render the ticket page (this will be your UI for showing active tickets)
@app.route("/mytickets")
def tickets_page():
    return render_template("tickets.html")

if __name__ == "__main__":
    app.run(debug=True)



# mongodb+srv://paras23:@KEQN9.s!@Yrr!7@cluster0.gblidbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
import random
import string

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("your_mongo_connection_string_here")  # Replace with actual URI
db = client["servicenowdb"]
tickets = db["tickets"]

# Generate random ticket number
def generate_ticket_number():
    return 'TKT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


# Show HTML form
@app.route('/form')
def show_form():
    return render_template("index.html")


# Handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    try:
        ticket_number = generate_ticket_number()
        data['ticketNumber'] = ticket_number
        tickets.insert_one(data)
        return jsonify({"message": "Form data saved successfully", "ticketNumber": ticket_number}), 200
    except Exception as e:
        return jsonify({"message": "Error saving form data", "error": str(e)}), 500


# Show ticket UI page (HTML)
@app.route('/tickets')
def tickets_page():
    return render_template("tickets.html")


# API to fetch all tickets
@app.route('/all-tickets')
def get_tickets():
    all_tickets = list(tickets.find({}, {'_id': 0}))
    return jsonify(all_tickets)


if __name__ == '__main__':
    app.run(debug=True)

from flask import request, redirect, jsonify

@app.route('/submit', methods=['POST'])
def submit_ticket():
    try:
        data = request.get_json()
        if not data:
            print("❌ No JSON data received")
            return jsonify({"message": "No data received"}), 400

        print("✅ Received data:", data)

        tickets.insert_one(data)
        print("✅ Ticket saved to database.")

        return redirect('/tickets')  # Redirect to the active tickets page

    except Exception as e:
        print("🔥 Error saving ticket:", str(e))
        return jsonify({"message": "Error saving ticket", "error": str(e)}), 500
