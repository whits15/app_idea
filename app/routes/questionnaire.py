from flask import Blueprint, jsonify, request
from app.utils.questionnaire import get_user_questionnaire
import os
import json
from datetime import datetime

questionnaire = Blueprint('questionnaire', __name__)

@questionnaire.route('/api/questionnaire', methods=['GET'])
def get_questionnaire():
    return jsonify(get_user_questionnaire())

@questionnaire.route('/api/load_test_data', methods=['GET'])
def load_test_data():
    try:
        with open('user_data/test_data.json', 'r') as f:
            test_data = json.load(f)
        return jsonify(test_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@questionnaire.route('/api/save_responses', methods=['POST'])
def save_responses():
    try:
        responses = request.get_json()
        if not responses:
            return jsonify({'error': 'No data provided'}), 400
        
        # Create user_data directory if it doesn't exist
        if not os.path.exists('user_data'):
            os.makedirs('user_data')
        
        # Save responses to a JSON file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"user_data/user_responses_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(responses, f, indent=4)
        
        return jsonify({'message': 'Responses saved successfully', 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 