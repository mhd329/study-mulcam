import json
from pprint import pprint


def movie_info(movie, genres):
    pass
    d={}
    for k,v in movie.items():
        if k == "id" or k == "title" or k == "vote_average" or k == "overview" :
            d[k]=v
        if k == "genre_ids":
            n= v
            list=[]
            for k in genres:
                for i in n:
                    if k['id'] == i:
                        list.append(k['name'])


            d['genre_names'] = list






    return d
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))