import json
from pprint import pprint


def movie_info(movie):
    result = {
        'id':movie.get('id'),
        'title':movie.get('title'),
        'vote_average':movie.get('vote_average'),
        'overview':movie.get('overview'),
        'genre_ids':movie.get('genre_ids')
    }
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('2회차/2회차-이호빈/이호빈/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))