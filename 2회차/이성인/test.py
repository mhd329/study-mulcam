import json
from pprint import pprint

genre_names =[]

def movie_info(movies, genres):
    n = len(genres)
    n2 = len(movies.get('genre_ids'))
    for i in range(n):
        for j in range(n2):
            if genres[i].get('id') == movies.get('genre_ids')[j]:
                genre_names.append(genres[i].get('name'))
    result = {
        'genre_names' : genre_names,
        'id' : movies.get('id'),
        'overview' : movies.get('overview'),
        'title' : movies.get('title'),
        'vote_average' : movies.get('vote_average'),
    }
    return result
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))