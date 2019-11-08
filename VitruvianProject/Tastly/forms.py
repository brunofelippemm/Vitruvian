from wtforms import Form, IntegerField, validators, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange

class InputForm(FlaskForm):
    age = IntegerField('Age', [validators.DataRequired(message=('Please enter your age')), validators.NumberRange(min=15, max=100, message=('Please enter a valid number'))])

    gender = SelectField('Gender',[validators.DataRequired(message=('Please select a gender'))], choices=[('male', 'Male'), ('female', 'Female')])

    music = SelectField('Music genre', [validators.DataRequired(message=('Please select a music genre'))], choices=[('rock', 'Rock'), ('pop', 'Pop'), ('electronic', 'Electronic'), ('country', 'Country')])

    beverage =  SelectField('Beverage', [validators.DataRequired(message=('Please select a beverage'))], choices=[('beer', 'Beer'), ('wine', 'Wine'), ('wiskey', 'Wiskey'), ('tequila', 'Tequila'), ('vodka', 'Vodka'), ('dosent drink', 'Doesnt drink')])

    smoke = SelectField('Do you smoke?', [validators.DataRequired(message=('Please select a smoking option'))], choices=[('yes', 'Yes'), ('no', 'No')]) 