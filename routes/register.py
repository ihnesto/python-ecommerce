from app import app
from flask import render_template, request, redirect, flash, url_for, session
from datetime import datetime
from datetime import timedelta
from flask_login import login_required
from models.product import Product
from forms.regform import RegistrationForm
from forms.logform import LoginForm

@app.route("/register", methods=['GET', 'POST'])
def register() :  
    # if current_user.is_authenticated:
    #     return redirect('/')
    form = RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user = User(username=form.firstName.data + form.lastName.data, email=form.email.data, password=hashed_password)
    #     db.session.add(user)
    #     db.session.commit()
    #     flash('Your account was created', 'success')
    #     return redirect('/login')
    return render_template('register.html', title='Register', form=form)
