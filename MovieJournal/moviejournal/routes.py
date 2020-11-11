from flask import render_template, url_for, request, redirect, flash
from moviejournal import app
from moviejournal.forms import MovieForm, JournalEntryForm
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

@app.route('/journal/<int:movie_id>', methods=['POST', 'GET'])
def journal(movie_id):
    form = JournalEntryForm()
    movie = MovieJournals.query.get(movie_id)
    entries = MovieJournals.query.get(movie_id).entries

    if form.validate_on_submit():
        sentiment = 1 # CALL THE MODEL HERE!!!
        
        entry = JournalEntry(entry=form.entry.data, sentiment=sentiment, journal_id=movie_id)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("journal", movie_id=movie_id))

    return render_template('journal.html', movie=movie, entries=entries, form=form)