from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField

class MovieForm(FlaskForm):
    title = StringField('Move Title', validators=[DataRequired(), Length(min=1, max=30)])
    year = IntegerField('Year released', validators=[DataRequired(), NumberRange(min=1890)])
    director = StringField('Director', validators=[DataRequired(), Length(min=2, max=20)])
    cover = FileField('Movie Cover')
    submit = SubmitField('Submit')
    