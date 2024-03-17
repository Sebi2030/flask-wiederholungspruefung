from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from flask_login import  LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

class User
id = db.Column(db.Integer, primary_key=True)
created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)


class Post



class Like