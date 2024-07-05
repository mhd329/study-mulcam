import json
from pprint import pprint


def movie_info(movie, genre_list):
    genre_num = movie.get('genre_ids')
    genre_convert = []
    for genre in genre_list:
        if genre['id'] in genre_num:
            genre_convert.append(genre['name'])

    result = {}
    key_list = ['id', 'title', 'vote_average', 'overview', 'genre_names']
    for key in  key_list:
        result[key] = movie.get(key, genre_convert)

    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))