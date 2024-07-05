# 영화 데이터 movie.json 와 genres.json 을  활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오. 
# id, title, vote_average, overview, genre_names로 결과를 만듭니다.

import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    gnames = []
    for i in movie['genre_ids']:
        for j in genres:
            if i == j['id']:
                gnames.append(j['name'])

    result = {'genre_names': gnames,
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'titile': movie.get('title'),
            'vote_average': movie.get('vote_average')}

    return result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))