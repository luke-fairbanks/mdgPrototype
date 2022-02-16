
from flask import Blueprint, render_template, request, redirect, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from sqlalchemy.exc import IntegrityError
from .forms import SignupForm, LoginForm
from .models import db, User 
from . import login_manager
from .routes import nav

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    #sign up page
    #GET requests serve sign-up page.
    #POST requests validate form and user creation
    form = SignupForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            username = form.username.data.lower().replace(" ","")
            user = User(
                first = form.first.data,
                last = form.last.data,
                username = username,
                email = form.email.data,
                dateOfBirth = form.dateOfBirth.data,
            )
            user.set_password(form.password.data)
            #try:
            db.session.add(user)
            db.session.commit() #creates new user
            """except IntegrityError:
                db.session.rollback()
                flash('Could not validate your request.')
                return redirect(url_for('auth_bp.signup'))"""

            login_user(user, remember=True) # immediatly logs in as this user
            return redirect(url_for('profile', username=user.username))
        flash('A user with that email address already exists.')
    return render_template(
        'signup.html',
        title='Create an account',
        form=form,
        nav=nav,
        template='signup-page',
        body = 'Sign up for an account'
    )

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    #login page for users who already have an account

    if current_user.is_authenticated:
        return redirect(url_for('profile', username=current_user.username))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user,remember=True)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('profile', username=current_user.username))
            #return redirect(next_page or url_for('app.profile', username = user.username))
        flash('Incorrect username/password combination')
        return redirect(url_for('auth_bp.login'))
    return render_template(
        'login.html',
        form=form,
        nav=nav,
        title='Enter your garage',
        template='login-page',
    )
@login_manager.user_loader
def load_user(user_id):
    # check if user is logged in on every page load
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    #redirect unauthorized users to login page
    flash('You must be logged in to view that page')
    return redirect(url_for('auth_bp.login'))