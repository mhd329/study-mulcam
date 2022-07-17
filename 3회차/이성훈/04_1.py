import json
from pprint import pprint


def movie_info(movie):
    result = {
        'genre_ids' : movie.get('genre_ids','NO RESULT'),
        'id' : movie.get('id','NO RESULT'),
        'overview' : movie.get('overview','NO RESULT'),
        'poster_path' : movie.get('poster_path', 'NO RESULT'),
        'title' : movie.get('title', 'NO RESULT'),
        'vote_average' : movie.get('vote_average', 'NO RESULT')
    }
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))