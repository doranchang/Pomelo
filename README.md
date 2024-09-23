# Pomelo Event Summary Service

This Flask-based web service is designed for the Pomelo coding exercise, allowing you to submit financial events and retrieve a summary of transactions. It provides endpoints for submitting events, getting a summary, retrieving all stored events, and clearing the stored data.

## Features

- Submit various types of events (transactions and payments)
- Retrieve a summary of the current state based on submitted events
- View all stored events
- Clear all stored events

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
Install Dependencies: Make sure you have Python and pip installed. Then, install Flask:

bash
Copy code
pip install Flask
Run the Application: Save the provided Flask code in a file named app.py, and run it:

bash
Copy code
python app.py
The application will start on http://127.0.0.1:5000.

Testing the Service
You can test the service using curl commands in your terminal. Here are some example commands to submit events and retrieve the summary:

Submit Events
Submit Transaction Authorized Event:

bash
Copy code
curl -X POST http://127.0.0.1:5000/submit_event \
-H "Content-Type: application/json" \
-d '{
  "creditLimit": 1000,
  "events": [
    {
      "eventType": "TXN_AUTHED",
      "eventTime": 1,
      "txnId": "t1",
      "amount": 123
    }
  ]
}'
Submit Transaction Settled Event:

bash
Copy code
curl -X POST http://127.0.0.1:5000/submit_event \
-H "Content-Type: application/json" \
-d '{
  "creditLimit": 1000,
  "events": [
    {
      "eventType": "TXN_SETTLED",
      "eventTime": 2,
      "txnId": "t1",
      "amount": 456
    }
  ]
}'
Submit Payment Initiated Event:

bash
Copy code
curl -X POST http://127.0.0.1:5000/submit_event \
-H "Content-Type: application/json" \
-d '{
  "creditLimit": 1000,
  "events": [
    {
      "eventType": "PAYMENT_INITIATED",
      "eventTime": 3,
      "txnId": "p1",
      "amount": -456
    }
  ]
}'
Submit Payment Posted Event:

bash
Copy code
curl -X POST http://127.0.0.1:5000/submit_event \
-H "Content-Type: application/json" \
-d '{
  "creditLimit": 1000,
  "events": [
    {
      "eventType": "PAYMENT_POSTED",
      "eventTime": 4,
      "txnId": "p1",
      "amount": 0
    }
  ]
}'
Get Summary
To retrieve the summary of transactions after submitting events, use the following command:

bash
Copy code
curl -X GET http://127.0.0.1:5000/get_summary
Additional Endpoints
Retrieve All Events:

bash
Copy code
curl -X GET http://127.0.0.1:5000/all_events
Clear All Events:

bash
Copy code
curl -X DELETE http://127.0.0.1:5000/clear
Conclusion
This Pomelo coding exercise showcases a simple yet effective way to manage and summarize financial events using a RESTful API. You can expand or modify it to meet specific requirements or additional features as needed.
