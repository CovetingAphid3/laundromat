from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from laundromat.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
# bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'users.info'


mail = Mail()





def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    # bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate = Migrate(app, db)
    from laundromat.main.routes import main
    from laundromat.users.routes import users
    from laundromat.orders.routes import orders
    from laundromat.admin.routes import administrator 
    from laundromat.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(orders)
    app.register_blueprint(administrator)
    app.register_blueprint(errors)
    
    from . import models
    with app.app_context():
        db.create_all()
    
    return app