from app.models import *
from flask import Flask,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin,LoginManager,login_user,login_required,logout_user
import os
# from dotenv import load_dotenv

# load_dotenv()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
# DB_USER=os.getenv('DB_USER')
# DB_PASSWORD=os.getenv('DB_PASSWORD')
# DB_HOST=os.getenv('DB_HOST')
# DB_PORT=os.getenv('DB_PORT')
# DB_BASE=os.getenv('DB_BASE')
app.config["SECRET_KEY"] = "My_Super_secret_Key"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}'
db = SQLAlchemy(app)
login_manager=LoginManager(app)
migrate=Migrate(app,db)
# login_manager.init_app(app)



from app.controlers import routes