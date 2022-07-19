import json
from pprint import pprint

from sqlalchemy import values


def movie_info(movie):
    li = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
    new_dict = {}
    for key, value in movie.items():
        if key in li:
            new_dict[key] = value
    
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))