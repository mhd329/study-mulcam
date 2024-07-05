import json
from pprint import pprint
from unicodedata import name


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
m =  open('data/movie.json','r',encoding='utf-8')
movie = json.load(m)
f =  open('data/genres.json','r',encoding='utf-8')
genres = json.load(f)
names = []


ids = movie['genre_ids']
for i in genres:
    if i['id'] in ids:
        names.append(i['name'])
summary = {'genre_names':names,'id':movie['id'],'overview':movie['overview'],'title':movie['title'],'vote_average':movie['vote_average']}
   
import sys
sys.stdout = open('05.txt','w',encoding='utf-8')
pprint(summary)


# 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     movie_json = open('data/movie.json', encoding='UTF8')
#     movie = json.load(movie_json)

#     genres_json = open('data/genres.json', encoding='UTF8')
#     genres_list = json.load(genres_json)

#     pprint(movie_info(movie, genres_list))