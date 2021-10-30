from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to News Article'
    return render_template('index.html', title = title)

@app.route('/source/<int:sources_id>')
def source(source_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('sources.html',id = source_id)