from flask_mail import Message
from app import mail
from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from flask_mail import Mail

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://cubinez85:123@localhost/testdb'

db = SQLAlchemy(app)

mail = Mail(app)

with app.app_context():

    msg = Message('test subject', sender='postfix@cubinez.ru',
    recipients=['cubinez65@yandex.ru'])
    msg.body = 'text body'
    msg.html = '<h1>HTML body</h1>'
    mail.send(msg)
