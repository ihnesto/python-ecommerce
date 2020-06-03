from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, FileField, RadioField, SelectField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import timedelta
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
import config

app = Flask(__name__)

app.config.from_object(config.EcommerceConfig)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    discount = db.Column(db.Float())
    image = db.Column(db.String(150))

    def __repr__(self):
        return f"Product({self.desc} - {self.price})"

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User({self.username} - {self.email})"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
    firstName = StringField('First name', validators=[ DataRequired() ])
    lastName = StringField('Last name', validators=[ DataRequired() ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Create password', validators=[DataRequired()])
    confirmPassword = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    genderMale = RadioField('gender', validators=[DataRequired()])
    genderFemale = RadioField('gender', validators=[DataRequired()])
    address = StringField('Address', validators=[ DataRequired() ])
    address2 = StringField('Address 2 (Optional)', validators=[ DataRequired() ])
    city = StringField('City', validators=[ DataRequired() ])
    zipCode = StringField('Zip', validators=[ DataRequired() ])
    country = SelectField('Country', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submitButton = SubmitField('Register')
    agreeTerms = BooleanField('', )

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is exists')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


@app.route("/register", methods=['GET', 'POST'])
def register() :  
    if current_user.is_authenticated:
        return redirect('/')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account was created', 'success')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data, duration = timedelta(days=5))
            next_page = request.args.get('next')
            if next_page :
                return redirect(next_page)
            else :
                return redirect('/')     
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
    # print(session)
    logout_user()
    return redirect('/')

@app.route('/')
def index() :
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__' :
    app.run(debug=True)


# def inserDataToDB():
#     p = ['Product name goes here just for demo item', 1280, "/static/images/main-page/" ]

#     for i in range(1, 10) :
#         prod = Product(desc=p[0], price=p[1], image=f'{p[2]}{i}.jpg')
#         db.session.add(prod)
#         db.session.commit()