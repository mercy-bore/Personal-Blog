import urllib.request,json
from app.models import Quote


# Getting api key
quotes_url = None

def configure_request(app):
    global quotes_url
    quotes_url = app.config['QUOTES_API_URL']
    
def get_quote(id):
    get_quote_details_url = quotes_url.format(id)
    with urllib.request.urlopen(get_quote_details_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)
        quote_object = None
        if quote_details_response:
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')
            quote_object = Quote(author,quote,)

    return quote_object

def process_quote_results(quote_list):
    
    quote_results = []
    for quote_item in quote_list:
        author = quote_item.get('author')
        quote = quote_item.get('quote')
        
   
        quote_object = Quote(author, quote)
        quote_results.append(quote_object)

    return quote_results
