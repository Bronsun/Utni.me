from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db,bcrypt
from neuro.NewUsers.forms import LoginForm, RegistrationForm
from neuro.modules import UserLink,User
from flask_login import login_user, current_user, logout_user,login_required

NewUsers=Blueprint('NewUsers',__name__)


###### Login Page ##### 
@NewUsers.route('/login',methods=['GET','POST'])

def login():
    error=None
    if current_user.is_authenticated:
        return redirect(url_for('Main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Main.index'))
        else:
            error="Nieprawidłowe hasło lub email"
    return render_template('login.html', title='Login', form=form,error=error)






###### Register Page ######
@NewUsers.route("/register", methods=['GET', 'POST'])
def register():
    error=None
    if current_user.is_authenticated:
        return redirect(url_for('Main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if request.form.get('agree')!=None:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(name=form.name.data, email=form.email.data, password=hashed_password,lastname=form.lastname.data,company=form.company.data)
            db.session.add(user)
            db.session.commit()            
            return redirect(url_for('NewUsers.login'))
        else:
            error="Aby się zarejestrować musisz zaakceptować warunki regulaminu"
    return render_template('register.html', title='Register', form=form,error=error)


######## LOGOUT ###########
@NewUsers.route('/logout')
def logout():
    logout_user()
    return redirect('login')
