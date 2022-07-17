import json
from pprint import pprint


def movie_info(movie):
    result = {
        'id': movie.get('id'), # movie.json 딕셔너리 파일에서 id를 가져옴
        'title': movie.get('title'),  
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_ids': movie.get('genre_ids')
        }
    return result # movie_info에 해당하는 result를 반환


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))