from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_dropzone import Dropzone
import os


app = Flask(__name__)


app.config['SECRET_KEY']='adsadsd3123kjhg32131iplksa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
dropzone= Dropzone(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'NewUsers.login'

from neuro.Account.routes import Account
from neuro.LinkConverterBasic.routes import LinkConvBasic
from neuro.LinkAdvanceConverter.routes import LinkAdvanceConverter
from neuro.Main.routes import Main
from neuro.NewUsers.routes import NewUsers
from neuro.PDF.routes import PDF

app.register_blueprint(Account)
app.register_blueprint(LinkConvBasic)
app.register_blueprint(LinkAdvanceConverter)
app.register_blueprint(Main)
app.register_blueprint(NewUsers)
app.register_blueprint(PDF)