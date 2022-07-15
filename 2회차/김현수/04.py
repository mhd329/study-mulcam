import json
from pprint import pprint


def movie_info(movie):
    return {'genre_ids' : movie.get('genre_ids'), #5줄이 계속 반복 되네 반복문으로 작성해보자
    'id': movie.get('id'),
    'overview': movie.get('overview'),
    'title': movie.get('title'),
    'vote_average': movie.get('vote_average')
    }
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))