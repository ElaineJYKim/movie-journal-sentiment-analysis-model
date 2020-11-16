# Sentiment Analysis Project
Bert_Model - notebooks used for Data Preprocessing, Model Training, Evaluating <

MovieJournal - Flask app for running the Movie Journal application

## Bert_Model
Final Model Used
- Colab Notebook: Bert_Model/Finetuning_Notebooks/RottenCasedTF.ipynb
- Dataset: [Rotten Tomatos Movie Reviews](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data)
- Bert Based Model: cased_L-12_H-768_A-12

This model has an overall accuracy of 0.76. The macro accuracy for this particular model isn't especially better than the other models. However, it was choosen because it's precision for the different target labels were fairly balanced and because it's recall favored Positive and Negative entries. I thought having better accuracy for + and - enteries would be more valable since most people using this service would be opinionated to one particular sentiment.


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

5) Insert Model.

**Currently model not behaving as expected. Saved model evaluations vastly differ from what is expected.**

⋅⋅1. Download [Model](https://works.do/xEAxdf)
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

