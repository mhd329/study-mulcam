import json
from pprint import pprint

# 'movie.json','genres.json'을 불러와 필요한 정보로만 구성된 딕셔너리 출력
def movie_info(movie, genres):
    info = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_names': []
    }

    for id in movie.get('genre_ids'):
        for genre in genres:
            if genre.get('id') == id:
                info['genre_names'].append(genre.get('name'))
                break
            
    return info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))