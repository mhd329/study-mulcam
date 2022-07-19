import json
from operator import ge
from pprint import pprint


def movie_info(movie, genres):
    genre_ids=movie['genre_ids']
    gerne_name=[]

    for genre in genres:
        if genre['id'] in genre_ids:
            gerne_name.append(genre['name'])
            

    key_list = ['id','title','vote_average','overview']
    movie_info_dict = {}

    for key in key_list:
        movie_info_dict[key] = movie[key]
    movie_info_dict['gerne_names'] = gerne_name

    return movie_info_dict
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('2회차/2회차-이호빈/이호빈/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('2회차/2회차-이호빈/이호빈/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))