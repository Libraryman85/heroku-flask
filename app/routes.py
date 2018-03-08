from flask import render_template

from app import app


@app.route('/index1')
def index1():
    user = {'username': 'Alex'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alex'}
    return render_template('index.html', title='Dashboard', adventurer=adventurer, games=games)
