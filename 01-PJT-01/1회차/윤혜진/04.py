import json
from pprint import pprint

# 'movie.json' 파일을 불러와 필요한 정보로만 구성된 딕셔너리를 출력
def movie_info(movie):
    info = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_ids': movie.get('genre_ids')
    }
    
    return info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))