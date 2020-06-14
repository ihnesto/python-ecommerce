from app import app
from flask import render_template, request, redirect, flash, url_for, session
from datetime import datetime
from datetime import timedelta
from flask_login import login_required
from models.product import Product
from forms.regform import RegistrationForm
from forms.logform import LoginForm


@app.route("/logout")
@login_required
def logout():
    # # print(session)
    # logout_user()
    return redirect('/')
