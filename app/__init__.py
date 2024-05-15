# app/__init__.py
from flask import Flask

app = Flask(__name__)

from app import balance_service, transaction_service, auditing_service, security_service
