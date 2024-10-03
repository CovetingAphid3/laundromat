import datetime
from laundromat import db, login_manager
from flask_login import UserMixin
import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone =  db.Column(db.String(13))
    is_admin= db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    orders = db.relationship('Orders', backref='user', lazy=True)
    address = db.relationship('Address', backref='user', lazy=True)

    def get_reset_token(self, expires_seconds=9000):
        s = Serializer(current_app.config['SECRET_KEY'], expires_seconds)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', {self.email}', '{self.is_admin}')"



class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone =  db.Column(db.String(13), nullable=False)
    service =  db.Column(db.String(12), nullable=False)
    date = db.Column(db.Date, nullable=False)
    pick_up_time = db.Column(db.Time, nullable=False)
    special_instructions = db.Column(db.String(250), nullable=True)
    image = db.Column(db.String(50), nullable=False, default='default.jpg')
    status = db.Column(db.String, default='Pending')
    address = db.Column(db.String)
    price = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Orders('{self.date}','{self.service}','{self.pick_up_time}', '{self.special_instructions}')"


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(250), nullable=False)
    complex = db.Column(db.String(250), nullable=True)
    suburb = db.Column(db.String(250), nullable=False)
    postal_code = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    def __repr__(self):
        return f"Address('{self.street_name}','{self.complex}','{self.suburb}', '{self.postal_code}', '{self.user_id}')"
    

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return f"Newsletter('{self.name}', '{self.email})"