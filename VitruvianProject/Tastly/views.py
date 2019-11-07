"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Tastly import app, TasteService

@app.route('/')
@app.route('/home')
def home():
	TasteService.findAll()
	return render_template(
		'landing.html',
		title='Wellcome to vitruvian',
		year=datetime.now().year,
	)

@app.route('/input')
def contact():
    """Renders the input page."""
    return render_template(
        'input.html',
        title='Input',
        year=datetime.now().year,
        message='Please insert your input'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
