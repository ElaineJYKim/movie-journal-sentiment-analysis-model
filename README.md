# Sentiment Analysis Project
Bert_Model - notebooks used for Data Preprocessing, Model Training, Evaluating <

MovieJournal - Flask app for running the Movie Journal application

## Bert_Model
Final Model Used
- Colab Notebook: Bert_Model/Finetuning_Notebooks/RottenTF.ipynb
- Dataset: [Rotten Tomatos Movie Reviews](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data)
- Bert Based Model: uncased_L-12_H-768_A-12


## MovieJournal
**Description**

- Create journals for different movies.
- Write entries for each journal.
- Have your journal entries be classified by sentiment (Negative, Neutral, Positive).


### Run App
1) Clone the repository and navigate to the folder.

2) (Optional) Create a virtual environment to install packages.

`virtualenv venv`

3) (Optional) Activate the virtual environment.

`source venv/bin/activate`

4) Install required packages.

`pip install -r requirements.txt`

5) Inset Model.

⋅⋅1. Download [Model](https://works.do/FXKHUP)
..2. Move model directory into **tf** directory (filepath: MovieJournal/moviejournal/tf)

6) Run the server.

Currently set to debug mode (Debug=True).

`python run.py`

7) Open your web browser and navigate to the webpage.


### Database
To Delete all current movie and journal data.

1) 
```python
>>> from moviejournal import db
>>> db.drop_all()
>>> db.create_all()
>>> exit()
```

2) Delete all movie cover files from **uploads** directory (filepath: MovieJournal/moviejournal/static/uploads)

