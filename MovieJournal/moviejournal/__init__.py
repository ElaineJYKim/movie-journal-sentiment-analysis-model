from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '87b48b92060727ca03b6f30f3b340661'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_PATH'] = 'moviejournal/uploads'
db = SQLAlchemy(app)

from moviejournal import routes