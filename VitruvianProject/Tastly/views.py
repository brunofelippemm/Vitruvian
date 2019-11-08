"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect
from Tastly.forms import InputForm
from wtforms import Form, IntegerField, SelectField 
from wtforms.validators import DataRequired
from Tastly import app, TasteService

@app.route('/')
@app.route('/home')
def home():
	return render_template(
		'landing.html',
		title='Wellcome to vitruvian',
		year=datetime.now().year,
	)

@app.route('/input')
def input():
    """inpun Form."""
    form = InputForm()
    """Renders the input page."""
    return render_template(
        'input_music.html',
        title='Input',
        year=datetime.now().year,
        message='Please insert your input',
        form= form
        )


@app.route('/results', methods=['POST', 'GET'])
def handle_data():
    form = InputForm()
    form.validate_on_submit()
    final_values = {}
    for info in form:
        final_values[info.name] = info.data
    print(final_values)
    return redirect("/")
    

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
