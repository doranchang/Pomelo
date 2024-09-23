from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            credit_limit INTEGER,
            event_type TEXT,
            event_time INTEGER,
            txn_id TEXT,
            amount INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Call this to initialize the database
init_db()

@app.route('/submit_event', methods=['POST'])
def submit_event():
    data = request.get_json()
    
    # Store the event in the database
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events (credit_limit, event_type, event_time, txn_id, amount) 
        VALUES (?, ?, ?, ?, ?)
    ''', (data["creditLimit"], data["eventType"], data["eventTime"], data["txnId"], data["amount"]))
    conn.commit()
    conn.close()

    return jsonify({"message": "Event submitted successfully."}), 200

@app.route('/get_summary', methods=['GET'])
def get_summary():
    current_state = summarize()
    return jsonify({"summary": current_state}), 200

@app.route('/all_events', methods=['GET'])
def all_events():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events')
    rows = cursor.fetchall()
    conn.close()

    # Format events as a list of dictionaries
    events_list = []
    for row in rows:
        events_list.append({
            "id": row[0],
            "credit_limit": row[1],
            "event_type": row[2],
            "event_time": row[3],
            "txn_id": row[4],
            "amount": row[5]
        })

    return jsonify({"events": events_list}), 200

@app.route('/clear', methods=['DELETE'])
def clear_events():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM events')
    conn.commit()
    conn.close()
    
    return jsonify({"message": "All events cleared."}), 200

def summarize():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute('SELECT credit_limit FROM events LIMIT 1')
    credit_limit = cursor.fetchone()
    if credit_limit:
        credit_limit = credit_limit[0]
    else:
        credit_limit = 0

    # Initialize variables for calculation
    available_credit = credit_limit
    payable_balance = 0
    pending_transactions = []
    settled_transactions = []

    # Fetch all events
    cursor.execute('SELECT event_type, event_time, txn_id, amount FROM events')
    rows = cursor.fetchall()

    transaction_map = {}
    payment_map = {}

    # Process events
    for row in rows:
        event_type = row[0]
        event_time = row[1]
        txn_id = row[2]
        amount = row[3]

        if event_type == "TXN_AUTHED":
            transaction_map[txn_id] = (event_time, amount)
            available_credit -= amount
            pending_transactions.append((txn_id, amount, event_time))

        elif event_type == "TXN_SETTLED":
            if txn_id in transaction_map:
                initial_time, initial_amount = transaction_map[txn_id]
                settled_transactions.append((txn_id, amount, initial_time, event_time))
                available_credit += initial_amount  # Re-add the initial amount
                available_credit -= amount  # Subtract the settled amount
                payable_balance += amount
                pending_transactions = [(tid, amt, time) for tid, amt, time in pending_transactions if tid != txn_id]
        elif event_type == "TXN_AUTH_CLEARED":
            if txn_id in transaction_map:
                initial_time, initial_amount = transaction_map.pop(txn_id)
                available_credit += initial_amount  # Clear the auth, add back to credit
                pending_transactions = [(tid, amt, time) for tid, amt, time in pending_transactions if tid != txn_id]
        elif event_type == "PAYMENT_INITIATED":
            payment_map[txn_id] = (event_time, amount)
            payable_balance += amount  # Add to payable balance (amount is negative)
            pending_transactions.append((txn_id, amount, event_time))
        elif event_type == "PAYMENT_POSTED":
            if txn_id in payment_map:
                initial_time, initial_amount = payment_map.pop(txn_id)
                available_credit -= initial_amount  # Reduce available credit
                pending_transactions = [(tid, amt, time) for tid, amt, time in pending_transactions if tid != txn_id]
                settled_transactions.append((txn_id, initial_amount, initial_time, event_time))
        elif event_type == "PAYMENT_CANCELED":
            if txn_id in payment_map:
                initial_time, amount = payment_map.pop(txn_id)
                payable_balance += -amount  # Reduce the payable balance
    # Format output
    output = []
    output.append(f"Available credit: ${available_credit}")
    output.append(f"Payable balance: ${payable_balance}")
    output.append("\nPending transactions:")
    for txn in pending_transactions:
        output.append(f"{txn[0]}: ${abs(txn[1])} @ time {txn[2]}")

    output.append("\nSettled transactions:")
    for txn in settled_transactions[:3]:  # Limit to 3 most recent
        output.append(f"{txn[0]}: ${txn[1]} @ time {txn[2]} (finalized @ time {txn[3]})")

    conn.close()
    return "\n".join(output)

if __name__ == '__main__':
    app.run(debug=True)
