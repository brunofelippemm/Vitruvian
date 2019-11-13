from wtforms import IntegerField, validators, SubmitField, SelectField, StringField 
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from Tastly.PersonalTaste import PersonalTaste

class InputForm(FlaskForm):
    age = IntegerField('Age', [validators.DataRequired(message=('Please enter your age')), validators.NumberRange(min=15, max=100, message=('Please enter a valid number'))])

    gender = SelectField('Gender',[validators.DataRequired(message=('Please select a gender'))], choices=[('male', 'Male'), ('female', 'Female')])

    music = SelectField('Music genre', [validators.DataRequired(message=('Please select a music genre'))], choices=[('rock', 'Rock'), ('pop', 'Pop'), ('electronic', 'Electronic'), ('country', 'Country')])

    beverage =  SelectField('Beverage', [validators.DataRequired(message=('Please select a beverage'))], choices=[('beer', 'Beer'), ('wine', 'Wine'), ('wiskey', 'Wiskey'), ('tequila', 'Tequila'), ('vodka', 'Vodka'), ('dosent drink', 'Doesnt drink')])

    smoker = SelectField('Do you smoke?', [validators.DataRequired(message=('Please select a smoking option'))], choices=[('yes', 'Yes'), ('no', 'No')])

    def toPersonalTaste(self):
        taste = PersonalTaste()
        taste.age = self.age.data
        taste.gender = self.gender.data
        taste.music = self.music.data
        taste.beverage = self.beverage.data
        taste.smoker = self.smoker.data
        return taste
    

class ConfirmForm(FlaskForm):
    gender = SelectField('Gender',[validators.DataRequired(message=('Please select a gender'))], choices=[('male', 'Male'), ('female', 'Female')])

    music = SelectField('Music genre', [validators.DataRequired(message=('Please select a music genre'))], choices=[('rock', 'Rock'), ('pop', 'Pop'), ('electronic', 'Electronic'), ('country', 'Country')])

    beverage =  SelectField('Beverage', [validators.DataRequired(message=('Please select a beverage'))], choices=[('beer', 'Beer'), ('wine', 'Wine'), ('wiskey', 'Wiskey'), ('tequila', 'Tequila'), ('vodka', 'Vodka'), ('dosent drink', 'Doesnt drink')])


