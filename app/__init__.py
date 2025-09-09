from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,login_required,logout_user,UserMixin
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///project.db"
app.config.from_object('config')
db= SQLAlchemy(app)
migrate = Migrate(app=app,db=db)
login_manager = LoginManager(app)

from app.models import tables
from .controllers.default import app

