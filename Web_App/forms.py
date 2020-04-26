from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class PlayerSelectionForm(FlaskForm):
    """User entry form for entering players on home/away teams"""
    # Home Team Players
    year_options = []
    for i in range(1990, 2020):
        year_options.append((i, f"{i}-{i + 1}"))

    home_year_1 = SelectField(validators=[DataRequired()], choices=year_options)
    home_1 = StringField('1)', validators=[DataRequired()])
    home_2 = StringField('2)', validators=[DataRequired()])
    home_3 = StringField('3)', validators=[DataRequired()])
    home_4 = StringField('4)', validators=[DataRequired()])
    home_5 = StringField('5)', validators=[DataRequired()])
    home_6 = StringField('6)')
    home_7 = StringField('7)')
    home_8 = StringField('8)')
    home_9 = StringField('9)')
    home_10 = StringField('10)')
    home_11 = StringField('11)')
    home_12 = StringField('12)')
    home_13 = StringField('13)')

    # Away Team Players
    away_1 = StringField('1)', validators=[DataRequired()])
    away_2 = StringField('2)', validators=[DataRequired()])
    away_3 = StringField('3)', validators=[DataRequired()])
    away_4 = StringField('4)', validators=[DataRequired()])
    away_5 = StringField('5)', validators=[DataRequired()])
    away_6 = StringField('6)')
    away_7 = StringField('7)')
    away_8 = StringField('8)')
    away_9 = StringField('9)')
    away_10 = StringField('10)')
    away_11 = StringField('11)')
    away_12 = StringField('12)')
    away_13 = StringField('13)')

    # Submit button
    submit = SubmitField('Predict')