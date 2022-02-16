from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

#globally accessable libraries
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    #core application
    app = Flask(__name__, template_folder='templates')
    app.config.from_object("config.DevelopmentConfig")

    #plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        #include routes
        from . import routes
        from . import auth

        db.create_all() # Create sql tables for our data models
        #register blueprints
        app.register_blueprint(auth.auth_bp)
        
        return app