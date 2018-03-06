from flask_runner import Manager

from app import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()


    def index():
        user = {'username': 'Miguel'}
        return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''
