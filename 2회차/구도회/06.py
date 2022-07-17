import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다. 
    id_name = {}
    for i in genres : 
        id_name[i['id']] = i['name']

    for n in range(len(movies)):
        genre_names = []
        for id in movies[n]['genre_ids']:
            genre_names.append(id_name[id])
        movies[n]['genre_names'] = genre_names

    result_new = []
    for m in range(len(movies)):
        result = {
        'id' : movies[m]['id'], 'title' : movies[m]['title'],
        'vote_average' : movies[m]['vote_average'], 
        'overview' : movies[m]['overview'],
        'genre_ids' : movies[m]['genre_ids']}
        result_new.append(result)
    return result_new  

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))