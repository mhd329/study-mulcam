import json
from pprint import pprint


def movie_info(movie):
    pass 
    f = open('data/movie.json', 'r', encoding = 'utf-8')
    g = json.load(f)
    result = {
        'genre_ids' : g.get('genre_ids'),
        'id' : g.get('id'),
        'overview' : g.get('overview'),
        'title' : g.get('title'),
        'vote_average' : g.get('vote_average')
    }
    pprint(result)
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))