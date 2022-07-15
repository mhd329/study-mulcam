import json
from operator import itemgetter
from pprint import pprint

def search_genre_name(movie, genres):
    genres_names = []
    genre_id = movie.get('genre_ids')
    for id in genre_id:
        for j in range(len(genres)):
            if (id == genres[j].get('id')):
                genres_names.append(genres[j].get('name'))
                break
    return (genres_names)

def movie_info(movies, genres):
    pass 

    res = []
    movies_list = sorted(movies, key=itemgetter('vote_average'), reverse=True)

    for movie in movies_list:
        search_name = search_genre_name(movie, genres)

        res.append({
            'genre_names': search_name,
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average')
    })
    return (res)
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))