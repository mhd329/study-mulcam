import json
from pprint import pprint


def movie_info(movie):
    pass 
    mine = {
        'genre_ids' : movie.get('genre_ids'),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'poster_path' : movie.get('poster_path'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')

    }
    for i, j in mine.items():
        print('{} : {}'.format(i, j))


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))