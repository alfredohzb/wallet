# app/transaction_service.py
from app import app
from app import balance_service

# Simulate a transactions database
transactions = []

@app.route("/transfer")
def transfer():
    sender = "user1"  # Example user sending the transfer - We can obtain this from the Authentication layer
    recipient = "user2"  # Example user receiving the transfer - This can be a parameters send by the user to the API request
    amount = 100  # Example amount to transfer

    # Check if sender's balance is enough for the transfer
    sender_balance = balance_service.get_balance(sender, 0)
    if sender_balance < amount:
        return "Transfer failed: Insufficient balance"
    sender_new_balance = balance_service.decrease_balance(sender, amount)
    recipient_new_balance = balance_service.increase_balance(recipient, amount)

    # Register the transaction
    transactions.append({"sender": sender, "recipient": recipient, "amount": amount})

    return "Transfer successful"
