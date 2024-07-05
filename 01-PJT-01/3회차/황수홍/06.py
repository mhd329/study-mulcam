import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    result = [] # 어떤영화 ?
    for movie in movies:
        movie_info = {
        'genre_names': [],
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')        
    }
        for id in movie.get('genre_ids'):
            for genre in genres:
                if genre.get('id') == id:
                    movie_info['genre_names'].append(genre.get('name'))

        result.append(movie_info)
    return result
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))