from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account create for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Đăng kí tài khoản', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
            flash(f'Login successful! Hello, {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful! Please check user infomation.', 'danger')
    return render_template('login.html', title='Đăng nhập', form=form)
