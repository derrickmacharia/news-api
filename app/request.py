from app import app
import urllib.request,json
from .models import sources

Sources = sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
            print(sources_results_list)
    return sources_results

# def get_source(id):
#     get_sources_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_sources_details_url) as url:
#         sources_details_data = url.read()
#         sources_details_response = json.loads(sources_details_data)

#         sources_object = None
#         if sources_details_response:
#             id = sources_details_response.get('id')
#             name = sources_details_response.get('name')
#             description = sources_details_response.get('description')
#             url = sources_details_response.get('url')
#             category = sources_details_response.get('category')
#             country = sources_details_response.get('country')

#             sources_object = Sources(id,name,description,url,category,country)

#     return sources_object

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

