from flask import render_template
from app import app
from app.models import sources
from .request import get_articles, get_sources



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    new_source = get_sources()
    business_source = get_sources()
    entertainment_source = get_sources()
    sports_source = get_sources()
    print(sources)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,new = new_source, business = business_source , entertainment = entertainment_source, sports = sports_source )

@app.route('/articles/<sources_id>')
def articles(sources_id):
    
    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_articles(sources_id)
    print(articles)
    
    return render_template('articles.html',articles = articles )
