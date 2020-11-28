from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db,bcrypt
from neuro.modules import User,UserLink
from neuro.Account.forms import DeleteForm
from flask_login import login_user, current_user, logout_user,login_required

Account = Blueprint('Account',__name__)

####### Main account page #######
@Account.route("/account",methods=['GET','POST'])
@login_required
def account():
    error=None
    username=current_user.name
    lastname=current_user.lastname
    email = current_user.email
    company=current_user.company
    return render_template('users.html',username=username,lastname=lastname,email=email,company=company,error=error)

###### DELETE ######
@Account.route("/delete",methods=['GET','POST'])
@login_required
def delete():
    form = DeleteForm()
    error=None
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            error="Nie ma takiego użytkownia"
        else:
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for('Main.index'))
    
    return render_template('delete.html',form=form)

######## Links #######
@Account.route('/links',methods=['GET','POST'])
@login_required
def links():
    
    users = User.query.all()
    return render_template('links.html',users=users)
