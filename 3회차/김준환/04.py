import json
from pprint import pprint


def movie_info(movie):
    pass 
    f = open('data/movie.json', 'r', encoding='utf-8')
    mv = json.load(f)
    result = {
        'id' : mv.get('id'),
        'title' : mv.get('title'),
        'vote_average' : mv.get('vote_average'),
        'overview' : mv.get('overview'),
        'genre_ids' : mv.get('genre_ids')
    }
    
    pprint(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))