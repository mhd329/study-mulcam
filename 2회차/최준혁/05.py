import json
from pprint import pprint


def movie_info(movie, genres):
    # movie
    # genres_list
    g_names = [] # name값 담을 리스트
    shawshank = movie
    for ids in shawshank.get('genre_ids'): # movie의 장르 id 18, 80
        for id in genres: # genres에서 
            if ids == id.get('id'): # movie의 genre_ids와 같은게 있으면
                g_names.append(id.get('name')) # 리스트에 추가 

    result = {
        'genre_names'  : g_names,
        'genre_ids'    : movie.get('genre_ids'),
        'overview'     : movie.get('overview'),
        'title'        : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    return result
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))





