from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from flask_login import  LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

class Post
id = db.Column(db.Integer, primary_key=True)
created = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
title = db.Column(db.String(120), nullable=False)
body = db.Column(db.Text, nullable=False)

likes = db.relationship('Like', back_populates='post', passive_deletes=True)

author_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"), nullable=False)
author = db.relationship('User', back_populates='posts')
 

class User



class Like