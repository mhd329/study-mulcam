# - 영화 데이터 `movies.json` 와 `genres.json` 을  활용하여 필요한 정보로만 구성된 리스트를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 리스트를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.  **(결과 예시 참고)**
#     - 개별 영화 데이터는 `id`, `title`, `vote_average`, `overview`, `genre_names`로 구성된 딕셔너리입니다.
#         - genre_names는 각 장르 정보를 값으로 가집니다.
#         - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

# **TIP. 이전 단계의 코드를 활용할 수 있습니다.**

import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    result2 = []
    
    for topmovie in movies:
        genre_names = []
        for i in topmovie['genre_ids']:
            for j in genres:
                if i == j['id']:
                    genre_names.append(j['name'])

        result = {
            'id': topmovie.get('id'),
            'title': topmovie.get('title'),
            'vote_average': topmovie.get('vote_average'),
            'overview': topmovie.get('overview'),
            'genre_names': genre_names
                }
        result2.append(result)
        
    return result2
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))