
from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField

from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class InputForm(Form):
    age = IntegerField('age', [validators.DataRequired(message=('Please enter your age'))])