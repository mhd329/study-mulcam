import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    id_name = {}
    for i in genres : 
        id_name[i['id']] = i['name']

    genre_names = []
    for id in movie['genre_ids']:
        genre_names.append(id_name[id])
    movie['genre_names'] = genre_names

    result = {
        'id' : movie['id'], 'title' : movie['title'],
        'vote_average' : movie['vote_average'], 
        'overview' : movie['overview'],
        'genre_ids' : movie['genre_ids']
    }
    return result   



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))