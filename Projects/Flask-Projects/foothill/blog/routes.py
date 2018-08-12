import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Christian Otieno',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': 'June, 2018'
    },
    {
        'author': 'Christian Otieno',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': 'July, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        HashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=HashedPassword)
        db.session.add(user)
        db.session.commit() 
        flash(f'Your account has been created, you are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
       user = User.query.filter_by(email=form.email.data).first()
       if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user, remember=form.remember.data)
           next_page = request.args.get('next')
           return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def SavePicture(form_picture):
    RandomHex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = RandomHex + f_ext
    PicturePath = os.path.join(app.root_path, 'static/ProfilePics/', picture_fn)
    
    OutputSize = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(OutputSize)
    i.save(PicturePath)

    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            PictureFile = SavePicture(form.picture.data)
            current_user.ImageFile = PictureFile
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    ImageFile = url_for('static', 
                        filename='ProfilePics/' + current_user.ImageFile)
    return render_template('account.html', 
                        title='Account', ImageFile=ImageFile, form=form)



@app.route("/post/new", methods=['GET','POST'])
@login_required
def NewPost():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('CreatePost.html',title='New Post')


