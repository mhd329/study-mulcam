import json
from pprint import pprint


def movie_info(movies, genres):
    result = []
    id_name = {}

    for i in genres :
        id_name[i['id']] = i['name']

    for j in range(len(movies)) :
        genre_name = []
        for k in movies[j]['genre_ids'] :
            genre_name.append(id_name[k])
        movies[j]['genre_names'] = genre_name

    for y in movies :
        mv = {}
        mv['genre_names'] = y['genre_names']
        mv['id'] = y['id']
        mv['overview'] = y['overview']
        mv['title'] = y['title']
        mv['vote_average'] = y['vote_average']
        result.append(mv)
    return result
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))