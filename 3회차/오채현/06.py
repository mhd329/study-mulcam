import json
from pprint import pprint
from unittest import result


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.

    moviesList = []
    for movie in movies:
        genresId = movie.get('genre_ids')
        genresNames = []
        for i in range(len(genres)):
            for j in range(len(genresId)):
                if genres[i].get('id') == genresId[j]:
                    genresNames.append(genres[i].get('name'))

        result = {
        'genre_names':  genresNames,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }
        # movie.update()
        moviesList.append(result)
    return moviesList


        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))