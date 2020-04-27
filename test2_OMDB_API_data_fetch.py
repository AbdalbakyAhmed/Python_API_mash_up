import requests_with_caching as req
import json

def get_movie_data (art_title):
    url = "http://www.omdbapi.com/"
    param = {}
    param['t'] = art_title
    param['r'] = 'json'
    
    omdbapi_page_cache = req.get(url, params=param)
    return (json.loads(omdbapi_page_cache.text))
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# print(get_movie_data("Venom"))
# get_movie_data("Baby Mama")

def get_movie_rating (dict_query):
    for i in dict_query['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            #print("........")
            return int(i['Value'][:2])
            #return int(i['Value'][:-1])
        else:
            pass
    return 0
    

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# print(get_movie_rating(get_movie_data("Deadpool 2")))

