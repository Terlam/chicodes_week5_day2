# Import the os module
import os

# Creation of base directory for application
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents\chicodes_sept2020\week_5\in_class
# Mac & Linux = Documents/chicodes_sept2020/week_5/in_class


# Config Class
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you wil never guess this....'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 