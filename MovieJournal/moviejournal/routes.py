from flask import render_template, url_for, request, redirect, flash
from moviejournal import app, db, model, tokenizer
from moviejournal.forms import MovieForm, JournalEntryForm
from moviejournal.models import MovieJournals, JournalEntry
import os

import tensorflow as tf
from tensorflow import keras
import numpy as np

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
        entry = form.entry.data
        sentiment =  model_predict(entry) # CALL THE MODEL HERE!!!
        
        entry = JournalEntry(entry=entry, sentiment=sentiment, journal_id=movie_id)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("journal", movie_id=movie_id))

    return render_template('journal.html', movie=movie, entries=entries, form=form)

def model_predict(text):

    text = [text]

    pred_tokens = map(tokenizer.tokenize, text)
    pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
    pred_token_ids = list(map(tokenizer.convert_tokens_to_ids, pred_tokens))
    
    pred_token_ids = map(lambda tids: tids +[0]*(app.config['MAX_SEQ_LEN']-len(tids)),pred_token_ids)
    pred_token_ids = np.array(list(pred_token_ids))

    prediction = model.predict(pred_token_ids).argmax(axis=-1)[0]
    return prediction.item()

@app.route('/delete_journal/<int:movie_id>')
def delete_journal(movie_id):
    
    if MovieJournals.query.get(movie_id).entries is not None:
        entries = MovieJournals.query.get(movie_id).entries
        
        for entry in entries:
            JournalEntry.query.filter_by(id=entry.id).delete()

    movie = MovieJournals.query.filter_by(id=movie_id)
    os.remove(movie.first().cover_file)
    movie.delete()

    db.session.commit()

    return render_template('home.html', movies=MovieJournals)
