import json
from pprint import pprint


def movie_info(movies, genres):
    pass

    result=[]
    for k in movies:
        d = {}
        if k["id"]:
            value = k['id']
            d['id']=value
        if k['title']:
            value = k['title']
            d['title']=value
        if k['vote_average']:
            value = k['vote_average']
            d['vote_average'] = value
        if k['overview']:
            value = k['overview']
            d['overview']=value
        if k ["genre_ids"]:
            n= k["genre_ids"]
            list=[]
            for k in genres:
                for i in n:
                    if k['id'] == i:
                        list.append(k['name'])

            d['genre_names'] = list
        result.append(d)
    return result
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))