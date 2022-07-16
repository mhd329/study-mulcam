import json
from pprint import pprint


def movie_info(movie, genres_list):
    pass 
    # 여기에 코드를 작성합니다.  
    movie_dict = {'genre_names': []}
    for key in movie:
        if key== 'id' or key== 'overview' or key== 'title' or key== 'vote_average':
            movie_dict.update({f'{key}': movie[key]})

    for id in movie['genre_ids']:
        for genre in genres_list:
            if id == genre['id']:
                movie_dict['genre_names'].append(genre['name'])

    return movie_dict

    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))