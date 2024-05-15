# app/balance_service.py
from app import app

# Simulate a balance database
wallets = {
    "user1": 1000,
    "user2": 500,
    "user3": 200
}

def get_balance(user_id):
    balance = wallets.get(user_id, 0)  # Get user balance, if not exists, balance is 0
    return balance

def increase_balance(user_id, deposit):
    wallets[user_id] = wallets.get(user_id, 0) + deposit

def decrease_balance(user_id, withdraw):
    wallets[user_id] -= withdraw

@app.route("/balance/<user_id>")
def get_balance_route(user_id):
    balance = get_balance(user_id)
    return f"Balance for {user_id}: ${balance}"
