import requests_with_caching as req
import json

# import sys

# msecs = 200000
# sys.setExecutionLimit(msecs)  #increase the run time


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


def get_sorted_recommendations (movielst):
    lst = get_related_titles(movielst)
    dic = dict()
    for i in lst:
        ratings = get_movie_rating(get_movie_data(i))
        dic[i] = ratings
    #print(dic)
    return [i[0] for i in sorted(dic.items(), key=lambda item: (item[1], item[0]), reverse=True)]# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

