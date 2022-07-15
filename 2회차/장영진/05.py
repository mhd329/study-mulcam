import json
from pprint import pprint


def movie_info(movie, genres):
    info = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview')
    }

    n = [] # 최종값을 저장할 리스트
    for i in movie['genre_ids']: # genre_ids가 18, 80 i는 18과 80을 순회
        for j in genres: # genres의 id를 순회
            if j['id'] == i: # j가 i의 값과 같다면 최종 리스트에 name을 추가
                n.append(j['name'])

    info['genres_names'] = n

    return info
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))