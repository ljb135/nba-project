from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class SelectionForm(FlaskForm):
    """User entry form for entering specifics for generation"""
    # Home Team Players
    home = []
    for i in range(0, 13):
        home.append(StringField(f'Player {i+1}', [DataRequired()]))

    # Away Team Players
    away = []
    for i in range(0, 13):
        away.append(StringField(f'Player {i+1}', [DataRequired()]))

    email = StringField('Email Here Please', [DataRequired()])

    # Submit button
    submit = SubmitField("Enter")
