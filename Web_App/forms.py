from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length


class PlayerSelectionForm(FlaskForm):
    """User entry form for entering players on home/away teams"""

    year_options = []
    for i in range(1990, 2020):
        year_options.append((str(i), f"{i}-{i + 1}"))

    # Home Team Players
    home_year_1 = SelectField(validators=[InputRequired()], choices=year_options)
    home_year_2 = SelectField(validators=[InputRequired()], choices=year_options)
    home_year_3 = SelectField(validators=[InputRequired()], choices=year_options)
    home_year_4 = SelectField(validators=[InputRequired()], choices=year_options)
    home_year_5 = SelectField(validators=[InputRequired()], choices=year_options)
    home_year_6 = SelectField(choices=year_options)
    home_year_7 = SelectField(choices=year_options)
    home_year_8 = SelectField(choices=year_options)
    home_year_9 = SelectField(choices=year_options)
    home_year_10 = SelectField(choices=year_options)
    home_year_11 = SelectField(choices=year_options)
    home_year_12 = SelectField(choices=year_options)
    home_year_13 = SelectField(choices=year_options)

    home_1 = SelectField('1)', validators=[InputRequired()], choices=[])
    home_2 = SelectField('2)', validators=[InputRequired()], choices=[])
    home_3 = SelectField('3)', validators=[InputRequired()], choices=[])
    home_4 = SelectField('4)', validators=[InputRequired()], choices=[])
    home_5 = SelectField('5)', validators=[InputRequired()], choices=[])
    home_6 = SelectField('6)', choices=[])
    home_7 = SelectField('7)', choices=[])
    home_8 = SelectField('8)', choices=[])
    home_9 = SelectField('9)', choices=[])
    home_10 = SelectField('10)', choices=[])
    home_11 = SelectField('11)', choices=[])
    home_12 = SelectField('12)', choices=[])
    home_13 = SelectField('13)', choices=[])

    # Away Team Players
    away_1 = SelectField('1)', validators=[InputRequired()], choices=[])
    away_2 = SelectField('2)', validators=[InputRequired()], choices=[])
    away_3 = SelectField('3)', validators=[InputRequired()], choices=[])
    away_4 = SelectField('4)', validators=[InputRequired()], choices=[])
    away_5 = SelectField('5)', validators=[InputRequired()], choices=[])
    away_6 = SelectField('6)', choices=[])
    away_7 = SelectField('7)', choices=[])
    away_8 = SelectField('8)', choices=[])
    away_9 = SelectField('9)', choices=[])
    away_10 = SelectField('10)', choices=[])
    away_11 = SelectField('11)', choices=[])
    away_12 = SelectField('12)', choices=[])
    away_13 = SelectField('13)', choices=[])

    away_year_1 = SelectField(validators=[InputRequired()], choices=year_options)
    away_year_2 = SelectField(validators=[InputRequired()], choices=year_options)
    away_year_3 = SelectField(validators=[InputRequired()], choices=year_options)
    away_year_4 = SelectField(validators=[InputRequired()], choices=year_options)
    away_year_5 = SelectField(validators=[InputRequired()], choices=year_options)
    away_year_6 = SelectField(choices=year_options)
    away_year_7 = SelectField(choices=year_options)
    away_year_8 = SelectField(choices=year_options)
    away_year_9 = SelectField(choices=year_options)
    away_year_10 = SelectField(choices=year_options)
    away_year_11 = SelectField(choices=year_options)
    away_year_12 = SelectField(choices=year_options)
    away_year_13 = SelectField(choices=year_options)

    # Submit button
    submit = SubmitField('Predict')
