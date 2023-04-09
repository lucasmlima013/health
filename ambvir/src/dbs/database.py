from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/pulse'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

banco = SQLAlchemy(app)

