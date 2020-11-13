from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from flask_wtf.file import FileField
from moviejournal.models import MovieJournals
from datetime import datetime

# MAX_SEQ_LEN = 78

def validate_movie(form, field):
    titles = MovieJournals.query.with_entities(MovieJournals.title)
    titles = [title[0].replace(" ", "").upper() for title in titles]
    if field.data.replace(" ","").upper() in titles:
        raise ValidationError('A journal for this Movie already exists.')

def validate_year(form, field):
    if field.data < 1888:
        raise ValidationError('First motion picture data back to 1888!')
    elif field.data > datetime.now().year:
        raise ValidationError('Thats a release date in the future!')

class MovieForm(FlaskForm):
    title = StringField('Move Title', validators=[DataRequired(), Length(min=1, max=30), validate_movie])
    year = IntegerField('Year released', validators=[DataRequired(), validate_year])
    director = StringField('Director', validators=[DataRequired(), Length(min=2, max=20)])
    cover = FileField('Movie Cover')
    submit = SubmitField('Submit')

class JournalEntryForm(FlaskForm):
    entry = TextAreaField('Entry', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Upload new entry')