import json
from pprint import pprint


def movie_info(movie, genres):
    pass
    # 여기에 코드를 작성합니다.

    genres_name = []

    for genre in genres:
        if genre['id'] in movie['genre_ids']:
            genres_name.append(genre['name'])

    result = {
        'genre_names': genres_name,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
    }
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('2회차/백솔비/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('2회차/백솔비/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
