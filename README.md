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
   ```
2. **Install Python, pip, and Flask**:
   Install Python, pip, and Flask.

3. **Start the server**:
   ```bash
   python app.py
   ```
   The application will start on http://127.0.0.1:5000.

## Testing:
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
To retrieve a summary of the resulting available credit, payable balance, and pending+settled transactions as a JSON response:
```bash
curl -X GET http://127.0.0.1:5000/get_summary
```
To see all previously submitted events:
```bash
curl -X GET http://127.0.0.1:5000/all_events
```
To clear all previously submitted events:
```bash
curl -X DELETE http://127.0.0.1:5000/clear
```

<img width="566" alt="Screenshot 2024-09-22 at 8 08 47 PM" src="https://github.com/user-attachments/assets/990f02e0-ab9b-4fdd-b91f-9636fed7def8">
<img width="561" alt="Screenshot 2024-09-22 at 8 09 26 PM" src="https://github.com/user-attachments/assets/5229d2be-4047-43f3-a1e2-4bfa441f7fe1">
<img width="561" alt="Screenshot 2024-09-22 at 8 09 46 PM" src="https://github.com/user-attachments/assets/75a6d72f-3a8f-4b21-8b39-1423b4835259">
<img width="567" alt="Screenshot 2024-09-22 at 8 21 25 PM" src="https://github.com/user-attachments/assets/ca79a29a-5834-44f1-9b4a-ae8f40546e28">
<img width="562" alt="Screenshot 2024-09-22 at 8 10 14 PM" src="https://github.com/user-attachments/assets/8fa658a6-4034-49af-830d-84c5ccce74ec">

