from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class PlayerSelectionForm(FlaskForm):
    """User entry form for entering players on home/away teams"""
    # Home Team Players
    home_1 = StringField('Home Player 1', validators=[DataRequired()])
    home_2 = StringField('Home Player 2', validators=[DataRequired()])
    home_3 = StringField('Home Player 3', validators=[DataRequired()])
    home_4 = StringField('Home Player 4', validators=[DataRequired()])
    home_5 = StringField('Home Player 5', validators=[DataRequired()])
    home_6 = StringField('Home Player 6')
    home_7 = StringField('Home Player 7')
    home_8 = StringField('Home Player 8')
    home_9 = StringField('Home Player 9')
    home_10 = StringField('Home Player 10')
    home_11 = StringField('Home Player 11')
    home_12 = StringField('Home Player 12')
    home_13 = StringField('Home Player 13')

    # Away Team Players
    away_1 = StringField('Away Player 1', validators=[DataRequired()])
    away_2 = StringField('Away Player 2', validators=[DataRequired()])
    away_3 = StringField('Away Player 3', validators=[DataRequired()])
    away_4 = StringField('Away Player 4', validators=[DataRequired()])
    away_5 = StringField('Away Player 5', validators=[DataRequired()])
    away_6 = StringField('Away Player 6')
    away_7 = StringField('Away Player 7')
    away_8 = StringField('Away Player 8')
    away_9 = StringField('Away Player 9')
    away_10 = StringField('Away Player 10')
    away_11 = StringField('Away Player 11')
    away_12 = StringField('Away Player 12')
    away_13 = StringField('Away Player 13')

    # Submit button
    submit = SubmitField('Predict')
