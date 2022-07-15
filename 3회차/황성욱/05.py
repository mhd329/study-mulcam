from ctypes.wintypes import HENHMETAFILE
import json
from pprint import pprint


def movie_info(movie, genres):
    li = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
    new_dict = {}
    for key, value in movie.items():
        if key in li:
            new_dict[key] = value

    for i in genres_list:
        for j in range(len(new_dict['genre_ids'])):
            if new_dict['genre_ids'][j] == i['id']:
                new_dict['genre_ids'][j] = i['name']
            
    return new_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))