# app/auditing_service.py
from app import app
from app import transaction_service

@app.route("/audit")
def audit():
    # Show all registered transactions
    return {"transactions": transaction_service.transactions}
