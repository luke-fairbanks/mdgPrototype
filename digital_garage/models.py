from email.policy import default
from enum import unique
from operator import index
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    #model for user accounts
    __tablename__ = 'mdgPrototype-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    first = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    last = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    walletId = db.Column(
        db.String(200),
        index=False,
        unique=True,
        nullable=True
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    profile_picture = db.Column(
        db.String(20),
        unique = False,
        nullable=True,
        default='default.jpg'
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )
    dateOfBirth = db.Column(
        db.Date,
        index=False,
        unique=False,
        nullable=False
    )
    """dateCreated = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False 
    )"""
    bio = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    assets = db.relationship('Asset', backref='mdgPrototype-users')
    """admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )"""
    def set_password(self, password):
        self.password = generate_password_hash(
            password,
            method='sha256'
        )
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    date_created = db.Column(db.Integer)
    show_on_profile = db.Column(db.Boolean, unique=False, default=True)
    owner_username = db.Column(db.Integer, db.ForeignKey('mdgPrototype-users.username'))

    def __repr__(self):
        return '<Asset #{}'.format(self.id)
