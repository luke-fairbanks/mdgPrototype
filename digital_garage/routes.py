from fileinput import filename

import os
import random
import secrets

from flask import current_app as app
from flask import Flask, url_for, render_template, redirect, flash, make_response, Blueprint, request, Markup, jsonify
from .email import send_email
from .forms import ContactForm, UpdateProfileForm, AddAssetForm, ShowAssetForm
from .models import db, User, Asset
from flask_login import current_user, login_required, logout_user   
from datetime import date 

nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'About', 'url': '/about'},
    {'name': 'Contact', 'url': '/contact'},
]  
items = [
    {'title': 'test1', 'id':'1', 'date':'today'},
    {'title': 'test2', 'date':'02/22/2022'},
    {'title': 'test3', 'date':'04/15/2016'},
    {'title': 'test4', 'date':'01/1/2022'},
    {'title': 'test5', 'date':'12/31/2021'}
]
nft_examples = [
    {'id':'#000002', 'owner':'cruz', 'date':'today','title':'auto','img':'example-nft1.png','price':round(random.uniform(0,4),2)},
    {'id':'#000001', 'owner':'luke', 'date':'2/22/2022', 'title':'dream car','img':'datsunExample.png','price':round(random.uniform(0,4),2)},
    {'id':'#000003', 'owner':'dade', 'date':'3/11/2022', 'title':'invest!','img':'porscheExample.png','price':round(random.uniform(0,4),2)}
]

@app.route('/')
def home():
    global nav
    global items
    global nft_examples
    auctionAssets = Asset.query.filter_by(show_on_profile=True).limit(8).all()

    #landing page
    return render_template(
        'homepage.html',
        nav=nav,
        title="Digital Garage Co.",
        description='Welcome to the gateway to your digital garage. Join thousands of users from all around the globe in the future of cars.',
        items=items,
        auctionAssets=auctionAssets,
        nft_examples = nft_examples
    )

@app.route('/about')
def about():
    global nav
    return render_template(
        'about.html',
        nav=nav
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
    picture_path = os.path.join(app.root_path, 'static/img/profile-images/', picture_fn)
    form_picture.save(picture_path)
    print("Picture is save at {}".format(picture_path))
    
    return picture_fn


@app.route('/user/<username>', methods=['GET', 'POST'])
def profile(username):
    global nav
    form = UpdateProfileForm()
    assetForm = AddAssetForm()
    showForm = ShowAssetForm()
    canEdit = False
    targetUser = User.query.filter_by(username=username).first()
    if targetUser is not None:
        if current_user.is_authenticated and current_user.username == username: 
                canEdit = True;
                if form.validate_on_submit():
                    if form.picture.data:
                        picture_file = save_profile_picture(form.picture.data)
                        current_user.profile_picture = picture_file
                        print("user profile picture saved!")
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
                elif form.picture.errors:
                    errorMessage = Markup("There was an error submitting the form: <br><code>{}</code>".format(form.picture.errors))
                    flash(errorMessage)

                """if assetForm.validate_on_submit():
                    print("bruh")
                    newAsset = Asset(name="test", date_created=date.today().strftime("%m-%d-%Y"),owner_username=current_user.username)
                    db.session.add(newAsset)
                    db.session.commit() #creates new asset"""

        userProfilePicture = url_for('static',filename='img/profile-images/' + targetUser.profile_picture)
        return render_template(
            'profile.html',
            title = username+' - Digital Garage Profile',
            nav=nav,
            targetUser = targetUser,
            userProfilePicture = userProfilePicture,
            form=form,
            canEdit=canEdit,
            assetForm = assetForm,
            showForm = showForm,
        )
    else:
        return render_template(
            "errorPages/404.html",
            title='User "{}" not found'.format(username),
            nav=nav
        )
"""@app.route('/auto/<id>')
def productPage(id):
    global nav
    targetProduct = Car.query.filter_by(id=id).first()
"""
@app.route('/asset/<assetId>', methods=['GET', 'POST'])
def asset_page(assetId):
    targetAsset = Asset.query.filter_by(id=assetId).first()
    targetOwner = User.query.filter_by(username=targetAsset.owner_username).first()
    ownerProfilePicture = url_for('static',filename='img/profile-images/' + targetOwner.profile_picture)


    if targetAsset is not None:
        ownerUsername = targetAsset.owner_username
        return render_template(
            "assetpage.html",
            nav=nav,
            title = "Asset "+assetId+" - Digital Garage Co.",
            targetAsset=targetAsset,
            ownerUsername= ownerUsername,
            ownerProfilePicture=ownerProfilePicture
        )
    else:
        return render_template(
            "errorPages/404.html",
            title='Asset "{}" not found'.format(assetId),
            nav=nav
        )
@app.route('/assetpost',methods=['GET','POST'])
def update_assets():
    if request.method == "POST":
        asset_data = request.get_json()
        
        assetId = asset_data[0]["AssetId"]
        assetShow = asset_data[1]["AssetShow"]
        assetDelete = asset_data[2]["AssetDelete"]
        if not assetDelete:
            targetAsset = Asset.query.filter_by(id=assetId).first()
            print(targetAsset)
            print(type(assetShow))
            targetAsset.show_on_profile = assetShow
            db.session.commit() #updates database
            print(assetShow)
            print(targetAsset.show_on_profile)
            results = {'processed':'true'}
        elif assetDelete:
            Asset.query.filter_by(id=assetId).delete()
            db.session.commit() #updates database
            results = {'deleted':'true'}
        return jsonify(results)
    
    return redirect(url_for('not_found'))        


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



#handle errors

@app.errorhandler(404)
def not_found(self):
    global nav
    #Page not found.
    return make_response(
        render_template("errorPages/404.html",        
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