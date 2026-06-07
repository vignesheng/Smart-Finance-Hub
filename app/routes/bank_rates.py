from flask import Blueprint, jsonify
from ..models import BankRate

bank_rates_bp = Blueprint('bank_rates', __name__, url_prefix='/bank-rates')

@bank_rates_bp.route('/', methods=['GET'])
def get_bank_rates():
    rates = BankRate.query.all()

    grouped = {}
    for r in rates:
        bank = r.bank_name
        if bank not in grouped:
            grouped[bank] = {'bank_name': bank}

        type_map = {
            'home loan':     'home_loan',
            'car loan':      'car_loan',
            'bike loan':     'bike_loan',
            'personal loan': 'personal_loan'
        }

        field = type_map.get(r.loan_type.lower(), r.loan_type)
        grouped[bank][field] = float(r.interest_rate)

    return jsonify(list(grouped.values())), 200
