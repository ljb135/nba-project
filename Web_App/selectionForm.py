from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class SelectionForm(FlaskForm):
    """User entry form for entering specifics for generation"""
    # Home Team Players
    home_1 = StringField('Player 1', [DataRequired()])
    home_2 = StringField('Player 2', [DataRequired()])
    home_3 = StringField('Player 3', [DataRequired()])
    home_4 = StringField('Player 4', [DataRequired()])
    home_5 = StringField('Player 5', [DataRequired()])
    home_6 = StringField('Player 6', [DataRequired()])
    home_7 = StringField('Player 7', [DataRequired()])
    home_8 = StringField('Player 8', [DataRequired()])
    home_9 = StringField('Player 9', [DataRequired()])
    home_10 = StringField('Player 10', [DataRequired()])
    home_11 = StringField('Player 11', [DataRequired()])
    home_12 = StringField('Player 12', [DataRequired()])
    home_13 = StringField('Player 13', [DataRequired()])

    # Away Team Players
    away_1 = StringField('Player 1', [DataRequired()])
    away_2 = StringField('Player 2', [DataRequired()])
    away_3 = StringField('Player 3', [DataRequired()])
    away_4 = StringField('Player 4', [DataRequired()])
    away_5 = StringField('Player 5', [DataRequired()])
    away_6 = StringField('Player 6', [DataRequired()])
    away_7 = StringField('Player 7', [DataRequired()])
    away_8 = StringField('Player 8', [DataRequired()])
    away_9 = StringField('Player 9', [DataRequired()])
    away_10 = StringField('Player 10', [DataRequired()])
    away_11 = StringField('Player 11', [DataRequired()])
    away_12 = StringField('Player 12', [DataRequired()])
    away_13 = StringField('Player 13', [DataRequired()])

    # Submit button
    submit = SubmitField("Enter")
