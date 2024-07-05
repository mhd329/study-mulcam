import json
from pprint import pprint


def movie_info(movie, genres):
    info = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview')
    }

    genre_name = [] # 최종 리스트
    for i in movie['genre_ids']: # i는 18과 80을 순회
        for j in genres: # j는 genres를 순회
            if j['id'] == i: # j['id']가 18과 20을 만나면 최종 리스트에 append
                genre_name.append(j['name'])

    # info['genres_names'] = genre_name

    return info
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))