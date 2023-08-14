from flask import Flask
from database import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///quze_api.db'

db.init_app(app)

