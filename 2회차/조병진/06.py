# JSON 데이터 활용 - 영화 다중 정보 활용
# 영화 데이터를 활용하여 필요한 정보로만 구성된 리스트를 출력하기
# 전체 영화 정보는 평점 높은 20개의 영화 데이터

import json
from pprint import pprint


def movie_info(movies, genres):
    pass
    # 여기에 코드를 작성합니다.

    result = []

    for movie in movies:
        for n in movie.get('genre_ids'):
            for i in genres:
                if n == i.get('id'):
                    a = []
                    a.append(i.get('name'))

        l = {
            'genre_names': a,
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average')
        }

        result.append(l)

    return result


pprint(movie_info)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
