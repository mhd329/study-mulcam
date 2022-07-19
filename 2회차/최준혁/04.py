import json
from pprint import pprint


def movie_info(movie):
    # genre_ids
    # overview
    # title
    # vote_average    
    shawshank = movie # 이름을 쇼생크라 짓고싶었어요
    result = {
        'genre_ids'     : shawshank.get('genre_ids'),
        'overview'      : shawshank.get('overview'),
        'title'         : shawshank.get('title'),
        'vote_average'  : shawshank.get('vote_average')
    }
    return result
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
