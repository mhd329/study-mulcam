import json
from pprint import pprint


def movie_info(movie):
    pass 

mo = open('data/movie.json','r',encoding='utf8')# 여기에 코드를 작성합니다.   
ge = open('data/genres.json','r',encoding='utf8')
mov = json.load(mo)
gen = json.load(ge)
gens = gen[0]
movs = mov[0]

r = { 'genre_ids': movs.get ('genre_ids'),
    #   'id' : gens.get('id'),
    #   'overview': movs.get ('overview'),
    #   'title': movs.get('title'),
    #   'vote_average': movs.get('vote_average'),
      } 
pprint(r)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))