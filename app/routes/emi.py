from flask import Blueprint, request, jsonify
from .. import db
from ..models import EmiCalc

emi_bp = Blueprint('emi', __name__, url_prefix='/emi')

@emi_bp.route('/calculate', methods=['POST'])
def calculate_emi():
    data = request.get_json()
    P = float(data['loan_amount'])
    R = float(data['interest_rate']) / 12 / 100
    N = int(data['tenure'])

    emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)

    record = EmiCalc(
        user_id=data.get('user_id'),
        loan_amount=P,
        interest_rate=data['interest_rate'],
        tenure=N,
        emi_result=round(emi, 2)
    )
    db.session.add(record)
    db.session.commit()

    return jsonify({'emi': round(emi, 2)}), 200
