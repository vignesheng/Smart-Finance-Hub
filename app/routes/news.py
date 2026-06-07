from flask import Blueprint, jsonify
from ..models import FinanceNews

news_bp = Blueprint('news', __name__, url_prefix='/news')

@news_bp.route('/', methods=['GET'])
def get_news():
    news = FinanceNews.query.order_by(FinanceNews.date.desc()).limit(10).all()
    result = [
        {
            'title': n.title,
            'description': n.description,
            'date': n.date.isoformat() if n.date else None
        }
        for n in news
    ]
    return jsonify(result), 200
