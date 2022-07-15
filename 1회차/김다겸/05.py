import json
from pprint import pprint


def movie_info(movie, genres):
    ids = movie['genre_ids']
    names = []

    for genre in genres:
        if genre['id'] in ids:
            names.append(genre['name']) 

    list = ['id', 'title', 'poster_path', 'vote_average', 'overview']
    dict = {}

    for key in list:
        dict[key] = movie[key]

    dict['gerne_names'] = names

    return dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))