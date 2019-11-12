"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect
from Tastly.forms import InputForm
from wtforms import Form, IntegerField, SelectField 
from wtforms.validators import DataRequired
from Tastly import app, TasteService
from Tastly import machine_learning
from Tastly.TasteService import findAll
import pandas as pd

@app.route('/')
@app.route('/home')
def home():
	return render_template(
		'landing.html',
		title='Wellcome to vitruvian',
		year=datetime.now().year,
	)

@app.route('/input-music')
def input_music():
    """inpun Form."""
    form = InputForm()
    chosen_feat = 'music'
    """Renders the input page."""
    return render_template(
        'input_music.html',
        title='Input',
        year=datetime.now().year,
        message='Please insert your input',
        form= form
        )

@app.route('/input-beverage')
def input_beverage():
    """inpun Form."""
    form = InputForm()
    chosen_feat = 'beverage'
    """Renders the input page."""
    return render_template(
        'input_beverage.html',
        title='Input',
        year=datetime.now().year,
        message='Please insert your input',
        form= form
        )

@app.route('/input-sex')
def input_sex():
    """inpun Form."""
    form = InputForm(),
    chosen_feat = 'sex'
    """Renders the input page."""
    return render_template(
        'input_sex.html',
        title='Input',
        year=datetime.now().year,
        message='Please insert your input',
        form= form
        )

@app.route('/results')
def result():
    """inpun Form."""
    form = InputForm()
    """Renders the input page."""
    return render_template(
        'results.html',
        title='Result',
        year=datetime.now().year,
        form= form
        )

    
@app.route('/results', methods=['POST', 'GET'])
def handle_data():
    form = InputForm()
    form.validate_on_submit()
    final_values = {}
    for info in form:
        final_values[info.name] = info.data
    final_values.pop(chosen_feat)
    final_values.pop('csrf_token')
    print(final_values)
    df = findAll()
    df.drop(columns= ['country'], inplace = True)
    prediction = machine_learning.feature_predict(final_values, df, chosen_feat)
    print(prediction)
    return redirect("/results")

@app.route('/confirm-results')
def confirm_result():
    """inpun Form."""
    form = ConfirmForm()
    """Renders the input page."""
    return render_template(
        'thank_you.html',
        title='Thank You',
        year=datetime.now().year,
        form= form
        )

@app.route('/confirm-results', methods=['POST', 'GET'])
def final_data():
    form = ConfirmForm()
    form.validate_on_submit()
    final_values = {}
    for info in form:
        final_values[info.name] = info.data
    print(final_values)
    return redirect("/confirm-results")

