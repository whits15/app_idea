from flask import Blueprint, jsonify

analysis = Blueprint('analysis', __name__)

@analysis.route('/api/analysis', methods=['POST'])
def analyze_responses():
    return jsonify({'message': 'Analysis endpoint'}), 200 