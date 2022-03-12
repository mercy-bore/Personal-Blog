import urllib.request,json
from app.models import Quote


# Getting quote url
quotes_url = None

def configure_request(app):
    global quotes_url
    quotes_url = app.config['QUOTES_API_URL']
    
def get_quote():
    get_quote = requests.get(quotes_url)
    response = []
    id = get_quote.get('id')
    author = get_quote.get('author')
    quote =get_quote.get('quote')
    
    quote_object = Quote(id,author,quote)
    response.append(quote_object)

    return response

