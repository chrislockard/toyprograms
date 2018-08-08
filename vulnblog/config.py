import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLAlchemy initilization, additional changes in app/__init__.py
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Enable CSRF protection in WTF Forms
WTF_CSRF_ENABLED = True
SECRET_KEY = '98fsjdll8HEUhKM,.@lkj*9dkdLaDf'

# OpenID providers
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id/<username>'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com/<username>'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com/<username>'}]

# Mail server settings
# Test these at the command prompt:
# python -m smtpd -n -c DebuggingServer localhost:25
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# Email administrator list
ADMINS = ['you@example.com']

# pagination for posts
POSTS_PER_PAGE = 5
