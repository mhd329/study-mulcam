import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다. 
    return result
    
m = open('./data/movie.json', 'r', encoding='utf-8')
o = json.load(m)
result = {
 'genre_ids' : o.get('genre_ids'),
 'id' : o.get('id'),
 'overview' : o.get('overview'),
 'title' : o.get ('title'),
 'vote_average' : o.get('vote_average')}


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))