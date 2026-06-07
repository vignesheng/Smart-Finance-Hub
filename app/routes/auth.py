from flask import Blueprint, request, jsonify
from .. import db
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'])
    user = User(name=data['name'], email=data['email'], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful', 'user_id': user.user_id}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/users/', methods=['GET'])
def get_users():
    users = User.query.order_by(User.created_at.desc()).limit(10).all()
    result = [
        {
            'name':   u.name,
            'email':  u.email,
            'status': 'Admin' if u.role == 'admin' else 'Active',
            'joined': u.created_at.strftime('%b %Y') if u.created_at else '—'
        }
        for u in users
    ]
    return jsonify(result), 200
