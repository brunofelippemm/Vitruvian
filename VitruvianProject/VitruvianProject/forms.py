from wtforms import Form, IntegerField, validators, SubmitField, SelectField

from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class InputForm(Form):
    age = IntegerField('Age', [validators.DataRequired(message=('Please enter your age'))])

    gender = SelectField('Gender',[validators.DataRequired(message=('Please select a gender'))], choices=[('male', 'Male'), ('female', 'Female')])

    musicGenre = SelectField('Music genre', [validators.DataRequired(message=('Please select a music genre'))], choices=[('rock', 'Rock'), ('pop', 'Pop'), ('electronic', 'Electronic'), ('country', 'Country')])

    beverage =  SelectField('Beverage', [validators.DataRequired(message=('Please select a beverage'))], choices=[('beer', 'Beer'), ('wine', 'Wine'), ('wiskey', 'Wiskey'), ('tequila', 'Tequila'), ('vodka', 'Vodka'), ('dosent drink', 'Doesnt drink')])

    smoke = SelectField('Do you somoke?', [validators.DataRequired(message=('Please select a smoking option'))], choices=[('yes', 'Yes'), ('no', 'No')]) 