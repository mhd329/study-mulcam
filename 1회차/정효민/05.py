import json
from pprint import pprint
from unittest import result


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    f = open('data/movies.json' , 'r' , encoding='utf-8')
    y = open('data/genres.json' , 'r' , encoding='utf-8')
    z = json.load(y)
    x = json.load(f)
    
    result = {
        'genres' : samsung.get('genres' ,)
    }
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))