import json
from pprint import pprint



def movie_info(movie):
    # 여기에 코드를 작성합니다.
    d={}
    for k,v in movie.items():
        if k == "id" or k == "title" or k == "vote_average" or k == "overview" or k == "genre_ids":
            d[k]=v


    return d


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))