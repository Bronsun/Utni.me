from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db,bcrypt
from neuro.modules import UserLink,User
from flask_login import login_user, current_user, logout_user,login_required
from flask_dropzone import Dropzone

Main = Blueprint('Main',__name__)


@Main.route('/')
def index():
    error=None
    
    if current_user.is_authenticated:
        userLink = UserLink.query.count()
        return render_template('main.html',userLink=userLink)
    else:    
        users=User.query.count()+2000
        currentUser=None
        link=UserLink.query.count()+1000
        x = request.remote_addr
    return render_template('main.html',link=link,users=users,x=x,error=error) 


@Main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404