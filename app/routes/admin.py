import re
from flask import Blueprint, jsonify

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

LOG_PATH = '/home/law/smart-finance-hub/logs/server.log'

@admin_bp.route('/stats', methods=['GET'])
def get_stats():
    try:
        with open(LOG_PATH, 'r') as f:
            content = f.read()

        blocks = [b.strip() for b in content.split('---') if b.strip()]
        last = blocks[-1] if blocks else ''

        cpu = re.search(r'CPU Usage:\s*([\d.]+)%', last)
        ram = re.search(r'RAM Usage:\s*(\d+)/(\d+) MB \(([\d.]+)%\)', last)
        disk = re.search(r'Disk Usage:\s*(\S+)', last)
        flask_status = re.search(r'Flask Status:\s*(\w+)', last)

        return jsonify({
            'cpu':         cpu.group(1) + '%' if cpu else '—',
            'ram':         ram.group(1) + '/' + ram.group(2) + ' MB' if ram else '—',
            'ram_percent': ram.group(3) if ram else '0',
            'disk':        disk.group(1) if disk else '—',
            'flask':       flask_status.group(1) if flask_status else '—'
        }), 200

    except FileNotFoundError:
        return jsonify({'error': 'Log file not found'}), 404

from ..models import User

@admin_bp.route('/user-stats', methods=['GET'])
def user_stats():
    from sqlalchemy import func
    total = User.query.count()
    active = User.query.filter_by(role='user').count()
    admin_count = User.query.filter_by(role='admin').count()
    inactive = total - active - admin_count

    return jsonify({
        'total': total,
        'active': active,
        'inactive': max(inactive, 0)
    }), 200
