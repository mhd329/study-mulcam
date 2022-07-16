import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    info = []
    for movie in movies:
        genres_name = []
        for genre in genres:
            if genre['id'] in movie['genre_ids']:
                genres_name.append(genre['name'])

        list = ['id', 'title', 'vote_average', 'overview']
        dict = {}

        for key in list:
            dict[key] = movie[key]
            dict['genre_names'] = genres_name
            info.append(dict)

    return info  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))