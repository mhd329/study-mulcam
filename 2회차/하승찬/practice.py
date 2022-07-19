import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
mo = open('data/movie.json','r',encoding='utf8') 
ge = open('data/genres.json','r',encoding='utf8')
mov = json.load(mo)
gen = json.load(ge)   #리스트 안에 인덱스가 있음
gens = gen
movs = mov
#id, title, vote_average, overview, genre_names



# for i in movs.get[i]:
#     if i in gen(
# i):
#         print(i)


print(list(m['name'] for m in gens))
# print(list(m.get['id']for m in gens))


    
# moveiv, genres의 id값과 대칭시켜 키값 가져오기

r = { 'genre_names': movs.get ('genre_names'),
      'id' : movs.get('id'),
      'overview': movs.get ('overview'),
      'title': movs.get('title'),
      'vote_average': movs.get('vote_average'),
      } 
pprint(r)
        
genid = movs.get("gere_ids")

print (genid)
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))