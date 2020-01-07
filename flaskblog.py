from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
