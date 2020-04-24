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
    home_6 = StringField('Player 6')
    home_7 = StringField('Player 7')
    home_8 = StringField('Player 8')
    home_9 = StringField('Player 9')
    home_10 = StringField('Player 10')
    home_11 = StringField('Player 11')
    home_12 = StringField('Player 12')
    home_13 = StringField('Player 13')

    # Away Team Players
    away_1 = StringField('Player 1', [DataRequired()])
    away_2 = StringField('Player 2', [DataRequired()])
    away_3 = StringField('Player 3', [DataRequired()])
    away_4 = StringField('Player 4', [DataRequired()])
    away_5 = StringField('Player 5', [DataRequired()])
    away_6 = StringField('Player 6')
    away_7 = StringField('Player 7')
    away_8 = StringField('Player 8')
    away_9 = StringField('Player 9')
    away_10 = StringField('Player 10')
    away_11 = StringField('Player 11')
    away_12 = StringField('Player 12')
    away_13 = StringField('Player 13')

    # Submit button
    submit = SubmitField("Enter")
