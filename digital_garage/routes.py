from fileinput import filename

import os
import secrets
from matplotlib.pyplot import title
from flask import current_app as app
from flask import Flask, url_for, render_template, redirect, flash, make_response, Blueprint, request
from .email import send_email
from .forms import ContactForm, UpdateProfileForm
from .models import db, User
from flask_login import current_user, login_required, logout_user    

nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'About', 'url': '/user/luke'},
    {'name': 'Contact', 'url': '/contact'},
]  


@app.route('/')
def home():
    global nav
    #landing page
    return render_template(
        'homepage.html',
        nav=nav,
        title="Digital Garage Com.",
        description='Welcome to the gateway to your digital garage.',
    )

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    global nav
    #contact form
    form = ContactForm()
    print(form.errors)
    if form.validate_on_submit():
        print('yeehaw ',form.name.data)
        name = form.name.data
        email = form.email.data
        body = form.body.data
        send_email(name, email, body)
        flash("Your message was sent!")
        return redirect(url_for("contact"))
    return render_template(
        'contactpage.html',
        form=form,
        nav=nav,
        title="Contact Us",
        description="We would love to hear from you! Feel free to contact us using the form below."
    )

#saving the input profile picture
def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/profile-images', picture_fn)
    form_picture.save(picture_path)
    
    return picture_fn


@app.route('/user/<username>', methods=['GET', 'POST'])
def profile(username):
    global nav
    form = UpdateProfileForm()
    canEdit = False
    targetUser = User.query.filter_by(username=username).first()
    if targetUser is not None:
        if current_user.is_authenticated and current_user.username == username: 
                canEdit = True;
                if form.validate_on_submit():
                    if form.picture.data:
                        picture_file = save_profile_picture(form.picture.data)
                        current_user.profile_picture = picture_file
                    current_user.first = form.first.data
                    current_user.last = form.last.data
                    current_user.username = form.username.data
                    current_user.email = form.email.data
                    current_user.bio = form.bio.data
                    db.session.commit()
                    flash('Your account has been updated!')
                    return redirect(url_for('profile',username=current_user.username))
                elif request.method == 'GET':
                    form.first.data = current_user.first
                    form.last.data = current_user.last
                    form.username.data = current_user.username
                    form.email.data = current_user.email
                    form.bio.data = current_user.bio

        userProfilePicture = url_for('static',filename='img/profile-images/' + targetUser.profile_picture)
        return render_template(
            'profile.html',
            title = 'Digital Garage Profile - '+username,
            nav=nav,
            targetUser = targetUser,
            userProfilePicture = userProfilePicture,
            form=form,
            canEdit=canEdit
        )
    else:
        return render_template(
            "errorPages/404.html",
            title='User "{}" not found'.format(username),
            nav=nav
        )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



#handle errors

@app.errorhandler(404)
def not_found():
    global nav
    #Page not found.
    return make_response(
        render_template("404.html",        
        title="We had trouble locating that page",
        nav=nav
        ),
        404,
        
     )

"""
@app.errorhandler(400)
def bad_request():
    #Bad request.
    return make_response(
        render_template("400.html"),
        400
    )


@app.errorhandler(500)
def server_error():
    #Internal server error.
    return make_response(
        render_template("500.html"),
        500
    )
"""