import json
from pprint import pprint
from this import d


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    result = {
        'genre_names': [],
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')        
    }
    for i in movie.get('genre_ids'):
        for genre in genres:
            if genre.get('id') == i:
                result['genre_names'].append(genre.get('name'))

    return result
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))