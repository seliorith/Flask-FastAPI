from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp


class RegistrationForm(FlaskForm):
    name = StringField('Name')
    surname = StringField('Surname')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8),
                                         Regexp('(?=.*[a-z])(?=.*[0-9])',
                                                message="Ошибка! Нужны цифры и буквы!")])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])

