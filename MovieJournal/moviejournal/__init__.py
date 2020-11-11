from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from moviejournal.tf.bert_tokenization import FullTokenizer
import tensorflow as tf
from tensorflow import keras
import os


global model, tokenizer
# load tokenizer and pre-trained model
model = tf.keras.models.load_model('moviejournal/tf/model')
tokenizer = FullTokenizer(vocab_file="moviejournal/tf/vocab.txt")

app = Flask(__name__)
app.config['SECRET_KEY'] = '87b48b92060727ca03b6f30f3b340661'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_PATH'] = 'moviejournal/static/uploads'
app.config['MAX_SEQ_LEN'] = 78 
db = SQLAlchemy(app)

from moviejournal import routes