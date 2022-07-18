import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    for id in genres:
        for a in genres:
            if a['id'] == id:
                print(id)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))