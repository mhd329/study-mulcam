import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
f =  open('data/movie.json','r',encoding='utf-8')
movie = json.load(f)
summary = {'genre_ids':movie['genre_ids'],'id':movie['id'],'overview':movie['overview'],'title':movie['title'],'vote_average':movie['vote_average']}
import sys
sys.stdout = open('04.txt','w',encoding='utf-8')
pprint(summary)


# 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     movie_json = open('data/movie.json', encoding='UTF8')
#     movie = json.load(movie_json)
    
#     pprint(movie_info(movie))