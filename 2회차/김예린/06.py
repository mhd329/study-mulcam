import json
from pprint import pprint


def movie_info(movies, genres):
    movie_info_dict = []

    for mlist in movies:
        genre_ids = mlist['genre_ids']
        genre_names = []

        for genre in genres:
             if genre['id'] in genre_ids:
                genre_names.append(genre['name'])

        movie_dict = {
            'genre_names': genre_names,
            'id': mlist['id'],
            'overview': mlist['overview'],
            'title': mlist['title'],
            'vote_average': mlist['vote_average'],
        }
        movie_info_dict.append(movie_dict)

    return movie_info_dict
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))