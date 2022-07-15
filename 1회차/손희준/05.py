import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
m =  open('data/movie.json','r',encoding='utf-8')
moive = json.load(m)
f =  open('data/genres.json','r',encoding='utf-8')
genres = json.load(f)
dic_gen = genres.split()
summary = {'genre_ids':moive['genre_ids'],'id':moive['id'],'overview':moive['overview'],'title':moive['title'],'vote_average':moive['vote_average']}

print(dic_gen)




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))