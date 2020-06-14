from app import app
from flask import render_template, request, redirect, flash, url_for, session
from datetime import datetime
from datetime import timedelta
from flask_login import login_required
from models.product import Product
from forms.regform import RegistrationForm
from forms.logform import LoginForm

@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect('/')
    form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data, duration = timedelta(days=5))
    #         next_page = request.args.get('next')
    #         if next_page :
    #             return redirect(next_page)
    #         else :
    #             return redirect('/')     
    #     else:
    #         flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    