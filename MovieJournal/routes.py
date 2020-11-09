from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import MovieForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '87b48b92060727ca03b6f30f3b340661'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class MovieJournals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(20), unique=False, nullable=False)
    cover_file = db.Column(db.String(20), unique=True, nullable=False)
    entries = db.relationship('JournalEntry', backref=, lazy=True)

    def __repr__(self):
        return f"MovieJournals('{self.title}', '{self.year}', '{self.director}', '{self.cover_file}')"

# entry maxed at 78 bc of model design - i was stupid
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(78), nullable=False)
    sentiment = db.Column(db.Intege, nullable=False)
    journal_id = db.Column(db.Integer, db.ForeignKey('.id'), nullable=False)

    def __repr__(self):
        return f"JournalEntry('{self.entry}', '{self.sentiment}', '{self.journal_id}')"


movies = [
    {
        'title': "The King",
        'year': 2019,
        'director': "David Michod",
        'sentiment': "Positive"
    },
    {
        'title': "the Grand Budapest Hotel",
        'year': 2014,
        'director': "Wes Anderson",
        'sentiment': "Neutral"
    }
]

app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', movies=movies)

@app.route('/add_movie', methods=['POST', 'GET'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():

        uploaded_file = request.files['cover']
        filename = form.title.data
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        
        # flash(f'New movie journal for {form.title.data} has been created', 'success')
        return redirect(url_for("home"))
    else:
        return render_template('add_movie.html', title="Add Movie", form=form)

@app.route('/tester')
def tester():
    flash('IS HTRAT YOU', 'ssuccess')
    return "hello world"

# just run with python
if __name__ == '__main__':
    app.run(debug=True)