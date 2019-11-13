"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, flash, request
from Tastly.forms import InputForm
from wtforms import Form, IntegerField, SelectField 
from wtforms.validators import DataRequired
from Tastly import app, TasteService, PersonalTaste
from Tastly import machine_learning
from Tastly import TasteService
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
    form = InputForm()
    """Renders the input page."""
    return render_template(
        'input_sex.html',
        title='Input',
        year=datetime.now().year,
        message='Please insert your input',
        form= form
        )



    
@app.route('/results', methods=['POST', 'GET'])
def handle_data():
	for key in request.form:
		if key.startswith('feat'):
			chosen_feat = key.partition('.')[-1]
	form = InputForm()
	form.validate_on_submit()
	taste = form.toPersonalTaste()
	print(taste.age)
	final_values = {}
	for info in form:
		final_values[info.name] = info.data
	final_values.pop(chosen_feat)
	final_values.pop('csrf_token')
	df = TasteService.findAll()
	prediction = machine_learning.feature_predict(final_values, df, chosen_feat)
	return render_template(
        'results.html',
        title='Result',
        year=datetime.now().year,
        form= form, 
        prediction = prediction,
        chosen_feat = chosen_feat,
		taste = taste.toString()
        )

@app.route('/confirm-results', methods=['POST', 'GET'])
def confirm_result():
	feat = request.form["confirmed_value"]
	taste = request.form["tentativeTaste"]
	print(taste)
	taste = PersonalTaste.fromString(taste)
	taste.fillValue(feat)
	"""Renders the input page."""
	TasteService.saveTaste(taste)
	return render_template(
        'thank_you.html',
        title='Thank You',
        year=datetime.now().year,
        )

@app.route('/correct-results', methods=['POST', 'GET'])
def final_data():
	feat = request.form["confirmed_value"]
	taste = request.form["tentativeTaste"]
	print(taste)
	taste = PersonalTaste.fromString(taste)
	form = InputForm()
	form.validate_on_submit()
	final_values = {}
	for info in form:
		final_values[info.name] = info.data
	print(final_values)
	return render_template(
        'thank_you.html',
        title='Thank You',
        year=datetime.now().year,
        )

