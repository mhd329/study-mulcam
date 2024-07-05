# JSON 데이터 활용 - 영화 단일 정보 응용
# 영화 데이터를 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하기

import json
from pprint import pprint


def movie_info(movie, genres):
    pass
    # 여기에 코드를 작성합니다.

    a = []
    for n in movie.get('genre_ids'):
        for i in genres:
            if n == i.get('id'):
                a.append(i.get('name'))

    result = {
        'genre_names': movie.get('genre_ids'),
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

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
