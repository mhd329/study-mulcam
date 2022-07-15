import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
f =  open('data/movie.json','r',encoding='utf-8')
moive = json.load(f)
summary = {'genre_ids':moive['genre_ids'],'id':moive['id'],'overview':moive['overview'],'title':moive['title'],'vote_average':moive['vote_average']}

import sys
sys.stdout = open('04.txt','w',encoding='utf-8')
pprint(summary)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))