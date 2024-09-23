# Pomelo Event Summary Service

I designed this Flask-based web service for the Pomelo coding exercise, allowing you to submit financial events and retrieve a summary of transactions. It provides endpoints for submitting events, getting a summary, retrieving all stored events, and clearing the stored data.

## Features

- Submit various types of events (transactions and payments)
- Retrieve a summary of the current state based on submitted events
- View all stored events
- Clear all stored events

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/doranchang/Pomelo
   cd Pomelo
Install Python, pip, and Flask.

python app.py
The application will start on http://127.0.0.1:5000.

Testing:
You can test the service using curl commands in your terminal. Here are some example commands to submit events:

   ```bash
   curl -X POST http://127.0.0.1:5000/submit_event \
   -H "Content-Type: application/json" \
   -d '{
     "creditLimit": 1000,
     "eventType": "TXN_AUTHED",
     "eventTime": 1,
     "txnId": "t1",
     "amount": 123
   }'
   
   curl -X POST http://127.0.0.1:5000/submit_event \
   -H "Content-Type: application/json" \
   -d '{
     "creditLimit": 1000,
     "eventType": "TXN_SETTLED",
     "eventTime": 2,
     "txnId": "t1",
     "amount": 456
   }'
   
   curl -X POST http://127.0.0.1:5000/submit_event \
   -H "Content-Type: application/json" \
   -d '{
     "creditLimit": 1000,
     "eventType": "PAYMENT_INITIATED",
     "eventTime": 3,
     "txnId": "p1",
     "amount": -456
   }'
   
   curl -X POST http://127.0.0.1:5000/submit_event \
   -H "Content-Type: application/json" \
   -d '{
     "creditLimit": 1000,
     "eventType": "PAYMENT_POSTED",
     "eventTime": 4,
     "txnId": "p1",
     "amount": 0
   }'
```
To retrieve a summary of the resulting available credit, payable balance, and pending+settled transactions:
curl -X GET http://127.0.0.1:5000/get_summary

To see all previously submitted events:
curl -X GET http://127.0.0.1:5000/all_events

To clear all previously submitted events:
curl -X DELETE http://127.0.0.1:5000/clear

