import json
from pprint import pprint


def movie_info():
    pass 
    # 여기에 코드를 작성합니다.
    movies_json = open('/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/data/movies.json', encoding='UTF8')
    movies = json.load(movies_json)

    genres_json = open('/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)
    
    
    for m in movies:
        print(m)    
    
    
movie_info()
# 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     movies_json = open('data/movies.json', encoding='UTF8')
#     movies_list = json.load(movies_json)

#     genres_json = open('data/genres.json', encoding='UTF8')
#     genres_list = json.load(genres_json)

#     pprint(movie_info(movies_list, genres_list))