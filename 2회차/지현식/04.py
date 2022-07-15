import json
from pprint import pprint


def movie_info(movie):
    key_list={'id','title','vote_average','overview','gener_ids'}
    movies={}
    for key in key_list:
        movies[key]=movie[key]
    return movies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))