from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length


class EventForm(FlaskForm):
    employees_count = IntegerField('Count of employees', validators=[DataRequired()])
    event_duration = FloatField('Duration of the meeting', validators=[DataRequired()])
    average_salary = IntegerField('Average salary (in rubles)', validators=[DataRequired()])
    submit = SubmitField('Calculate')


class SearchForm(FlaskForm):
    q = StringField('Search', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')
