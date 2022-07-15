import json
from pprint import pprint


def movie_info(movie):
    pass 
    f = open('data/movie.json','r',encoding = 'utf-8')
    m = json.load(f)
    ids = m['genre_ids']
    id = m['id']
    view = m['overview']
    ti = m['title']
    vo = m['vote_average']
    result = {
        'genre_ids' : ids,
        'id' : id,
        'overview' : view,
        'title' : ti,
        'vote_average' : vo
        
    }
    pprint(result)
    

   

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))