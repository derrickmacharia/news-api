from flask import render_template
from app import app
from .request import get_sources


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    source = get_sources()
    # print(source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,sources = source)

@app.route('/sources/<int:sources_id>')
def sources(sources_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('sources.html',id = sources_id)