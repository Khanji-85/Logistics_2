from flask import Blueprint, flash, redirect, render_template, request, url_for
import flask_login
from forms import login_form, registration_form
import models
import services
from app import login_manager

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET','POST'])
def register(): 
    form = registration_form()
    if request.method == 'POST':
        user = models.User()
        if form.validate_on_submit():
            user.username = form.user_name.data
            user.email = form.email.data
            user.password = form.password.data
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.phone_number = form.phone_number.data
            if(services.registration_service(user) == True):
                flash(f"Register successfully {form.email.data}","success")
                redirect(url_for("main.home"))
                return redirect(url_for("auth.login"))
            else:
                flash(f"Register Faild","danger")
    return render_template('registration.html',title='register',form = form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form()
    if request.method == 'POST' and form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash(f"Login success {form.email.data}", "success")
            flask_login.login_user(user)
            return redirect(url_for("main.home_page"))
        else:
            flash("Login failed", "danger")
    return render_template("login.html", title="Login", form=form)

@auth.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized():
    """Handles unauthorized access to protected resources."""
    return redirect(url_for('auth.login')), 401

@login_manager.user_loader
def load_user(user_id):
    """Loads the user object from the user ID stored in the session."""
    return models.User.get(user_id)