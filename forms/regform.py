from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, FileField, RadioField, SelectField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .all_countries import countries

class RegistrationForm(FlaskForm):
    firstName = StringField('First name', validators=[ DataRequired() ])
    lastName = StringField('Last name', validators=[ DataRequired() ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Create password', validators=[DataRequired()])
    confirmPassword = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    gender = RadioField('', choices=[('m', 'Male'), ('f', 'Female')], validators=[DataRequired()])
    address = StringField('Address', validators=[ DataRequired() ])
    address2 = StringField('Address 2 (Optional)', validators=[ DataRequired() ])
    city = StringField('City', validators=[ DataRequired() ])
    zipCode = StringField('Zip', validators=[ DataRequired() ])
    country = SelectField('Country', choices=countries, validators=[ DataRequired() ])
    submitButton = SubmitField('Register')
    agreeTerms = BooleanField('agreecheck')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is exists')

