from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from neuro.modules import UserLink

class ShortURLForm(FlaskForm):
    url = StringField(validators=[DataRequired()])
    submit = SubmitField('Skróć mnie !')

class CustomURLForm(FlaskForm):
    custom_name= StringField(validators=[DataRequired()])
    submit = SubmitField('Skróć mnie !')

