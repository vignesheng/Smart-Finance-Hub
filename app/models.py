from . import db
from datetime import datetime
from sqlalchemy import Enum

class User(db.Model):
    __tablename__ = 'USERS'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(Enum('user', 'admin', name='user_roles'), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class EmiCalc(db.Model):
    __tablename__ = 'EMI_CALC'

    emi_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id'), nullable=True)
    loan_amount = db.Column(db.Numeric(15, 2), nullable=False)
    interest_rate = db.Column(db.Numeric(5, 2), nullable=False)
    tenure = db.Column(db.Integer, nullable=False)
    emi_result = db.Column(db.Numeric(15, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class StockData(db.Model):
    __tablename__ = 'STOCK_DATA'

    stock_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Numeric(15, 2), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class MetalPrice(db.Model):
    __tablename__ = 'METAL_PRICES'

    metal_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Numeric(15, 2), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class BankRate(db.Model):
    __tablename__ = 'BANK_RATES'

    rate_id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(100), nullable=False)
    interest_rate = db.Column(db.Numeric(5, 2), nullable=False)
    loan_type = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


class FinanceNews(db.Model):
    __tablename__ = 'FINANCE_NEWS'

    news_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class ChatbotLog(db.Model):
    __tablename__ = 'CHATBOT_LOG'

    chat_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.user_id'), nullable=True)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
