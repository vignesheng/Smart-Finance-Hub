import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from app import create_app, db
from app.models import StockData
from dotenv import load_dotenv

load_dotenv()
app = create_app()

YF_SYMBOLS = [
    ('TCS',        'TCS.NS'),
    ('RELIANCE',   'RELIANCE.NS'),
    ('INFY',       'INFY.NS'),
    ('WIPRO',      'WIPRO.NS'),
    ('HDFCBANK',   'HDFCBANK.NS'),
    ('ICICIBANK',  'ICICIBANK.NS'),
    ('BAJFINANCE', 'BAJFINANCE.NS'),
    ('SBIN',       'SBIN.NS'),
    ('MARUTI',     'MARUTI.NS'),
    ('TITAN',      'TITAN.NS'),
    ('NIFTY50',   '^NSEI'),
    ('SENSEX',    '^BSESN'),
    ('BANKNIFTY', '^NSEBANK'),
    ('MIDCAP',    '^NSEMDCP50'),
]

def fetch_yahoo(name, symbol):
    try:
        import yfinance as yf
        ticker = yf.Ticker(symbol)
        data = ticker.history(period='1d', interval='1m')
        if not data.empty:
            price = float(data['Close'].iloc[-1])
            return price
        else:
            print(f'[NO DATA] {name}')
            return None
    except Exception as e:
        print(f'[YF ERROR] {name}: {e}')
        return None

with app.app_context():

    print('\n--- Fetching indices from Yahoo Finance ---')
    for name, yf_sym in YF_SYMBOLS:
        price = fetch_yahoo(name, yf_sym)
        if price:
            direction = '▲'
            print(f'{direction} {name}: {price:,.2f}')
            db.session.add(StockData(symbol=name, price=price))

    db.session.commit()
    print('\nAll stocks and indices updated successfully.')
