from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from neuro.modules import User

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Length(min=4,max=20)])
    name = StringField('Imię', validators=[DataRequired(),Length(max=20)])
    lastname = StringField('Nazwisko', validators=[DataRequired(),Length(max=40)])
    company = StringField('Nazwa firmy', validators=[Length(max=40)])
    password = PasswordField('Hasło', validators=[DataRequired(),Length(min=8,max=16,message='Hasło musi mieć od 8 do 16 znaków oraz składać się  z dużych liter i cyfr')])
    confirm_password = PasswordField('Powtórz hasło', validators=[DataRequired(),EqualTo('password','Hasło się nie zgadza ')])
    submit = SubmitField('Zarejstruj się')
    

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).all()
        if user:
            raise ValidationError('Użytkownik już istnieje')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')
    remember = BooleanField('Zapamiętaj mnie')