import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    x = open('data/movie.json','r',encoding='utf-8')
    mov = json.load(x)
    y = open('data/genres.json','r',encoding='utf-8')
    gen = json.load(y)
    num = mov['genre_ids']
    


    dic = {'genre_name' : gen['id']}

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))