import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from app import create_app, db
from app.models import FinanceNews
from dotenv import load_dotenv

load_dotenv()

app = create_app()
API_KEY = os.getenv('NEWS_API_KEY')

with app.app_context():
    try:
        url = f'https://newsapi.org/v2/everything?q=finance+india+stock&sortBy=publishedAt&pageSize=10&apiKey={API_KEY}'
        res = requests.get(url).json()
        articles = res.get('articles', [])
        for article in articles:
            title = article.get('title', '')[:255]
            description = article.get('description', '')
            if title:
                record = FinanceNews(title=title, description=description)
                db.session.add(record)
        db.session.commit()
        print(f"News updated: {len(articles)} articles")
    except Exception as e:
        print(f"Error fetching news: {e}")
