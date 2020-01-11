from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '9cb4001f74093f5ef54e8e8ffbec3400'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #Nói cho login_manager biết rằng route nào là login
login_manager.login_message_category = 'info' #Bootstrap required -- Please log in to access this page.

from flaskblog import routes