from database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    
    # nullable serves to indicate fields mandatory fill.
    # the parameter unique serves to indicate that information can't be repeated
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
