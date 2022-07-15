import json
from pprint import pprint
from re import A


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    result = []
    ele ={}
    key= [id, genre_names, overview, title ,vote_average]

    for movies in movie :
        for k in key:
            ele[k] = movies.get(k)
            result.append(ele)
    return result
pprint(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))