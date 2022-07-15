import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    id_name = {}
    for name in genres :
        id_name[name['id']] = name['name']

    for i in range(len(movies)):
        genre_names = []
        for id in movies[i]['genre_ids']:
            genre_names.append(id_name[id])
        movies[i]['genre_names'] = genre_names
    
    new_result = []
    for k in range(len(movies)):
        result = {
            'id' : movies[k]['id'],
            'title' : movies[k]['title'],
            'vote_average' : movies[k]['vote_average'],
            'overview' : movies[k]['overview'],
            'genre_names' : movies[k]['genre_names']
        }
        new_result.append(result)

    return new_result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))