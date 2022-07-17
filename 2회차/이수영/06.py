import json
from pprint import pprint


def movie_info(movies, genres):
    movie_info_dict = []

    for mylist in movies:
        genre_ids = mylist['genre_ids']
        genre_names = []

        for genre in genres:
             if genre['id'] in genre_ids:
              genre_names.insert(0, genre['name'])

        movie_dict = {
            'genre_names': genre_names,
            'id': mylist['id'],
            'overview': mylist['overview'],
            'title': mylist['title'],
            'vote_average': mylist['vote_average'],
        }
        movie_info_dict.append(movie_dict)

    return movie_info_dict
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))