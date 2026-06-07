# in your auth.py or a new users.py route
@auth_bp.route('/users/', methods=['GET'])
def get_users():
    users = User.query.order_by(User.created_at.desc()).limit(10).all()
    result = [
        {
            'name':   u.name,
            'email':  u.email,
            'status': 'Active',  # or u.status if you have that column
            'joined': u.created_at.strftime('%b %Y') if u.created_at else '—'
        }
        for u in users
    ]
    return jsonify(result), 200
