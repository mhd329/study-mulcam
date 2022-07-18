import json
from pprint import pprint


def movie_info(movie, genres):
    mov_list = []
    for a in genres_list:
        if a.get('id') in movie.get('genre_ids'):
          mov_list.append(a.get('name'))
          result = {
        'genre_names' :mov_list,
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' :movie.get('vote_average')
        }
    return result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))