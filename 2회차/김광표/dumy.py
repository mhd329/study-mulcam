import json
from pprint import pprint

movies_json = open('data/movie.json', encoding='UTF8')
movies_list = json.load(movies_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)

def genres_info(movies, genres) :
    genres_name = []
    for genres in genres_list :
        
        for movie_g in movies['genre_ids'] :
            if genres['id'] == movie_g :
                genres_name.append(genres['name'])
    return genres_name

print(genres_info(movies_list, genres_list))