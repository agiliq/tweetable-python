import urllib3

def get_quote_of_the_day():
    http = urllib3.PoolManager()
    resp = http.request('GET', 'https://quotes.rest/qod')
    return resp['contents']['quotes'][0]['quote']
