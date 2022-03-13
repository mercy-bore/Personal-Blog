
from .models import Quote
import urllib.request, json

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    '''
    '''
    url = base_url
    
    res = urllib.request.urlopen(url)
    data = json.loads(res.read())

    response=[]

    author = data.get('author')
    quote = data.get('quote')

    new_quote = Quote(author,quote)
    response.append(new_quote)

    return response