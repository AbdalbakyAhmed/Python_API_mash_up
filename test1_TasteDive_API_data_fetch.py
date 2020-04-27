import requests_with_caching as req
import json


def get_movies_from_tastedive (art_title):
    url = "https://tastedive.com/api/similar"
    param = dict()
    param['q'] = art_title
    param['type'] = 'movies'
    param['limit'] = 5
    
    tastedive_page_cache = req.get(url, params = param)
    return json.loads(tastedive_page_cache.text)
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# print(get_movies_from_tastedive("Bridesmaids"))
# get_movies_from_tastedive("Black Panther")

def extract_movie_titles (dict_query):
    lst_titles = list()
    for i in dict_query['Similar']['Results']:
        lst_titles.append(i['Name'])
    return lst_titles
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# print(extract_movie_titles(get_movies_from_tastedive("Tony Bennett")))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))

def get_related_titles (movielst):
    lst = list()
    for movie in movielst:
        lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(lst))


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# print(get_related_titles(["Black Panther", "Captain Marvel"]))
# get_related_titles([])


