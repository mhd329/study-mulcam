# JSON 데이터 활용 - 영화 단일 정보
# 영화 데이터를 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하기

import json
from pprint import pprint


def movie_info(movie):
    pass
    # 여기에 코드를 작성합니다.
    result = {
        'genre_ids': movie.get('genre_ids'),
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }

    pprint(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    pprint(movie_info(movie))
