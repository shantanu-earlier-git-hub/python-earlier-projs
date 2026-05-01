from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='../static', template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
import web_app.todo
db.init_app(app)
