from datetime import datetime
import string
from random import choices
from neuro import db ,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)
    lastname = db.Column(db.String(60), unique=False, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60),unique=True,nullable=False)
    company = db.Column(db.String(60),nullable=True)
    links = db.relationship('UserLink', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.name}','{self.lastname}', '{self.password}','{self.email}','{self.company}')"


class UserLink(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    original_url = db.Column(db.String(2000))
    short_url = db.Column(db.String(7),unique=True,nullable=True)
    custom_url = db.Column(db.String(500),unique=True,nullable=True)
    custom_name = db.Column(db.String(2000),unique=True,nullable=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()
        #self.custom_url = self.generate_custom_url()
        #self.custom_name = self.generate_custom_url()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=7))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        return short_url

