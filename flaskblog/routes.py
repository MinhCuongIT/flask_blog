from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2019',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'The post content the second',
        'date_posted': 'April 22, 2019',
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 3',
        'content': 'The post content the third',
        'date_posted': 'April 23, 2019',
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 4',
        'content': 'The post content the fourth',
        'date_posted': 'April 25, 2019',
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Trang Chủ')


@app.route('/about')
def about():
    return render_template('about.html', title='Về chúng tôi')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.username.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Đăng kí tài khoản', form=form)


@app.route('/login', methods=['GET', 'POST'])
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
            flash(f'Login unsuccessful! Please check email and password.', 'danger')
    return render_template('login.html', title='Đăng nhập', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Tài khoản')
