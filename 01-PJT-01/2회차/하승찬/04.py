# - 영화 데이터 `movie.json` 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - `id`, `title`, `vote_average`, `overview`, `genre_ids`으로 구성된 결과를 만듭니다.

import json
from pprint import pprint


def movie_info(movie):
    pass 

mo = open('data/movie.json','r',encoding='utf8') 
ge = open('data/genres.json','r',encoding='utf8')
mov = json.load(mo) # 4,5번 문제를 헷갈림, 
gen = json.load(ge)
gens = gen  # movie.json 파일의 인덱스는 하나이므로 번호추가 x
movs = mov

r = { 'genre_ids': movs.get ('genre_ids'),
      'id' :  movs.get('id'),
      'overview': movs.get ('overview'),
      'title': movs.get('title'),
      'vote_average': movs.get('vote_average'),
      } 
pprint(r)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))