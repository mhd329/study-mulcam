import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다. 
    temp_list = []
    movie_list = []
    
    for movie in movies:
        if movie['id'] in [278, 238, 424]:
            temp_list.append(movie)
    for movie in temp_list:
        genre_ids = movie['genre_ids']
        movie = {
            'genre_names': [],
            'id': movie['id'],
            'overview': movie['overview'],
            'title': movie['title'],
            'vote_average': movie['vote_average']
        }
        for genre_id in genre_ids:
            for genre_dict in genres:
                if genre_id == genre_dict['id']:
                    movie['genre_names'].append(genre_dict['name'])
        movie_list.append(movie)
        
    return(movie_list)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))