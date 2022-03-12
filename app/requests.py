import json,requests
from app.models import Quote


# Getting quote url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']
    
def get_quote():
    res = requests.get(base_url)
    
    response = []
    id = res.get('id')
    author = res.get('author')
    quote = res.get('quote')
    
    quote_object = Quote(id,author,quote)
    response.append(quote_object)

    return response

