# Python_API_mash_up

Process of mashing up data from two different APIs to make movie recommendations.
The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items.
https://tastedive.com/read/api
The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
https://www.omdbapi.com/
Puting those two together: 
1. use TasteDive to get related movies for a whole list of titles. 
2. combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

*To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. 
Just use requests_with_caching.get() rather than requests.get().

## Functions:
#### 1. def get_movies_from_tastedive (art_title):
takes one input parameter, a string that is the name of a movie or music artist. 
The function should return the 5 TasteDive results that are associated with that string; 
Only get movies, not other kinds of media. It will be a python dictionary with just one key.
#### 2. def extract_movie_titles (dict_query):
A function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive()
#### 3. def get_related_titles (movielst):
It takes a list of movie titles as input. 
It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list.

#### 4. def get_movie_data (art_title):
##### Fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
It takes in one parameter which is a string that should represent the title of a movie you want to search. 
The function returns a dictionary with information about that movie.
#### 5. def get_movie_rating (dict_query):
It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer.
#### 6. def get_sorted_recommendations (movielst):
It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function.

## Authors:
Ahmed Rabie Ahmed. abdalbaky.ahmed@gmail.com

*Final Project of the course Data Collection and Processing with Python
This course is part of the "Python 3 Programming Specialization" by University of Michigan.
more information: https://www.coursera.org/learn/data-collection-processing-python/home/welcome
