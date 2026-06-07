from flask import Blueprint, jsonify
from ..models import StockData

stocks_bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@stocks_bp.route('/', methods=['GET'])
def get_stocks():
    stocks = StockData.query.order_by(StockData.date.desc()).limit(20).all()
    result = [
        {
            'symbol': s.symbol,
            'price': str(s.price),
            'date': s.date.isoformat() if s.date else None
        }
        for s in stocks
    ]
    return jsonify(result), 200
