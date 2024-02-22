from flask import render_template
from app import app

@app.route('/')
def index():
  user = {'username': 'Jack'}
  return render_template('index.html', title='Home', user=user)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404