from flask import Blueprint, jsonify
from ..models import MetalPrice

metals_bp = Blueprint('metals', __name__, url_prefix='/metals')

@metals_bp.route('/', methods=['GET'])
def get_metals():
    metals = MetalPrice.query.order_by(MetalPrice.date.desc()).limit(10).all()
    result = [
        {
            'type': m.type,
            'price': str(m.price),
            'date': m.date.isoformat() if m.date else None
        }
        for m in metals
    ]
    return jsonify(result), 200
