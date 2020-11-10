from flask import render_template, url_for, request, redirect, flash
from moviejournal import app
from moviejournal.forms import MovieForm
from moviejournal.models import MovieJournals, JournalEntry
from moviejournal import db
import os


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', movies=MovieJournals)

@app.route('/add_movie', methods=['POST', 'GET'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():

        uploaded_file = request.files['cover']
        filename = form.title.data
        file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(file_path)
        
        movie = MovieJournals(title=filename, year=form.year.data, director=form.director.data, cover_file=file_path)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("home"))

    else:
        return render_template('add_movie.html', title="Add Movie", form=form)

@app.route('/tester')
def tester():
    flash('IS HTRAT YOU', 'ssuccess')
    return "hello world"