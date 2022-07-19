import json
from pprint import pprint

def movie_info(movies, genres):
    key_list = ['id', 'title', 'vote_average', 'overview', 'genre_names']
    result = []
   
    for movie in movies:
        elements = {}
        genre_convert = []
        for genre in genres:
            if genre['id'] in movie.get('genre_ids'):
                genre_convert.append(genre['name'])
        for key in key_list:
            elements[key] = movie.get(key, genre_convert)
        result.append(elements)

    return result

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))