from flask import Blueprint, send_from_directory
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return send_from_directory('static', 'index.html')

@main.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@main.route('/dashboard')
@login_required
def dashboard():
    return send_from_directory('static', 'index.html') 