from marvel_phonebook_app import app,db, login_manager

# Import all of the Werkzeg security methods
from werkzeug.security import generate_password_hash, check_password_hash

# Import for DateTime Module (This comes from python)
from datetime import datetime

# Import for the Login Manager UserMixin
from flask_login import UserMixin

# the user class will have
# An id, username, email 
# password, post

# Create the current user_manager using the user_loader function
# Which is a decorator(used in this class to send info to the User Model)
# Specifically the User's ID

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.String(150), primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique=True)
    phone = db.Column(db.String(15), nullable = False, unique=True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship('Post', backref = 'author', lazy = True)

    def __init__(self,username,phone,email,password):
        self.username = username
        self.phone = phone
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):

        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.username} has been created with the following email {self.email}'


# Creation of the Post Model
# The Post model will have an
# id, title, content, date_created
# user_id
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,title,content,user_id):
        self.title = title
        self.content=content
        self.user_id = user_id

    def __repr__(self):
        return f'The title of the post is {self.title} \n and the content is {self.content}'
