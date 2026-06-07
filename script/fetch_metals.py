import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
from app import create_app, db
from app.models import MetalPrice
from dotenv import load_dotenv

load_dotenv()
app = create_app()
API_KEY = os.getenv('GOLD_API_KEY')

with app.app_context():
    metals = [
        ('XAU', 'gold'),
        ('XAG', 'silver'),
        ('XPT', 'platinum'),
        ('XPD', 'palladium'),
    ]
    for code, metal_type in metals:
        try:
            res = requests.get(
                f'https://www.goldapi.io/api/{code}/INR',
                headers={'x-access-token': API_KEY}
            ).json()
            raw_price = res.get('price')
            if raw_price:
                price_10g = round(float(raw_price) / 3.215, 2)
                record = MetalPrice(type=metal_type, price=price_10g)
                db.session.add(record)
                print(f'{metal_type}: ₹{price_10g}')
            else:
                print(f'{metal_type} - no price: {res}')
        except Exception as e:
            print(f'Error fetching {code}: {e}')
    db.session.commit()
    print('All metals updated')
