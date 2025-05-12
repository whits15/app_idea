from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
import os

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Configure the app
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///user_data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints
    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.questionnaire import questionnaire
    from app.routes.analysis import analysis
    from app.routes.chat import chat
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(questionnaire)
    app.register_blueprint(analysis)
    app.register_blueprint(chat)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app 