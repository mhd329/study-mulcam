import json
from pprint import pprint


def movie_info(movie, genres):
    a = {}
    for i in movie :
        if i == 'id' or i == 'title'or i =='vote_average'or i == 'overview' or i == 'genre_ids' :
            a[i] = movie[i]
    for i in movie :
        if i == 'genre_ids' :
            a['genre_names']= []
            for j in a[i] :
                for k in range(len(genres)) :
                    if j == genres[k]['id'] :
                        a['genre_names'].append(genres[k]['name'])
    a.pop('genre_ids')
    return a
               



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))