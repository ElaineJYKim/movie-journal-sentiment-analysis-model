from datetime import datetime
from moviejournal import db


class MovieJournals(db.Model):

    __tablename__ = 'journal'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(20), unique=False, nullable=False)
    cover_file = db.Column(db.String(20), unique=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    entries = db.relationship('JournalEntry', backref='movie', lazy=True)

    def __repr__(self):
        return "MovieJournals('{}', '{}', '{}', '{}')".format(self.title, self.year, self.director, self.cover_file)

# entry maxed at 78 bc of model design - i was stupid
class JournalEntry(db.Model):

    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(78), nullable=False)
    sentiment = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    journal_id = db.Column(db.Integer, db.ForeignKey('journal.id'), nullable=False)

    def __repr__(self):
        return "JournalEntry('{}', '{}', '{}')".format(self.entry, self.sentiment, self.journal_id)