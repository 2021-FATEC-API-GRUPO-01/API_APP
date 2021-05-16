from flask import Flask
from flask_script import Manager
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate, MigrateCommand
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from flask_wtf  import  FlaskForm 
from  wtforms  import  StringField, PasswordField, TextAreaField, SubmitField, IntegerField, SelectField, FloatField, DecimalField
from wtforms.validators import InputRequired, Length, AnyOf, DataRequired
from flask_login import LoginManager
from sqlalchemy.sql import select
from decimal import ROUND_UP

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app)
manager = Manager(app)
mysql = MySQL(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)



from .models import models_spc
from app.controllers import index


