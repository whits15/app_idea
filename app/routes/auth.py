from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/api/auth/login', methods=['POST'])
def login():
    return jsonify({'message': 'Login endpoint'}), 200

@auth.route('/api/auth/register', methods=['POST'])
def register():
    return jsonify({'message': 'Register endpoint'}), 200 