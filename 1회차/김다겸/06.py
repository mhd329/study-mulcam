import json
from pprint import pprint


def movie_info(movies, genres):
    movies_list = []

    for movie in movies:
        ids = movie['genre_ids']
        names = []

        for genre in genres:
            if genre['id'] in ids:
                names.append(genre['name']) 

        list = ['id', 'title', 'poster_path', 'vote_average', 'overview']
        dict = {}

        for i in list:
            dict[i] = movie[i]

        dict['gerne_names'] = names
        movies_list.append(dict)

    return movies_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))