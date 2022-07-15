import json
from pprint import pprint


def movie_info(movie, genres):            
    genre_ids = movie.get('genre_ids') # [18, 80]
    genre_list = []
    result = {}
    for genre in genres:  # {} in []
        if genre['id'] in genre_ids:
            genre_list.append(genre['name'])

    key_list = ['genre_names', 'id', 'overview', 'title', 'vote_average']
    for key in key_list:
        result[key] = movie.get(key, genre_list)    
    return result

    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))