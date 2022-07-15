import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.
    movie_info_list = []

    for m in movies:
        genre_ids = m['genre_ids']
        genre_names = []

        for genre in genres:
            if genre['id'] in genre_ids:
                genre_names.append(genre['name'])
        
        movie_info = {
        'id' : m.get('id'),
        'title' : m.get('title'),
        'vote_average' : m.get('vote_average'),
        'overview' : m.get('overview'),
        'genre_names' : genre_names
        }

        movie_info_list.append(movie_info)
    
    return movie_info_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))