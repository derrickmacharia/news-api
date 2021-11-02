
import urllib.request,json
from .models import Sources,Articles


# Getting api key
api_key = ''
# Getting the movie base url
base_url_sources = None
base_url_articles = None

def configure_request(app):
    global api_key,base_url_sources,base_url_articles
    base_url_sources = app.config['NEWS_API_BASE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=def39ff22c2543fbbc005d7eaa87b661'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
            # print(sources_results_list)
    return sources_results


def process_results(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        country = sources_item.get('country')

        if id:
            sources_object = Sources(id,name,description,url,category,country)
            sources_results.append(sources_object)

    return sources_results


def get_articles(sources_id):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=def39ff22c2543fbbc005d7eaa87b661'.format(sources_id)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
            
    # print(articles_results_list)        
    return articles_results 


def process_articles(articles_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    articles_results = []
    for sources_item in articles_list:
        name = sources_item.get('name')
        description = sources_item.get('description')
        author = sources_item.get('author')
        url = sources_item.get('url')
        title = sources_item.get('title')
        urlToImage = sources_item.get('urlToImage')
        content = sources_item.get('content')
        publishedAt = sources_item.get('publishedAt')


        articles_object = Articles(id,name,description,author,url,title,urlToImage,content,publishedAt)
        articles_results.append(articles_object)


    return articles_results