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


genid = movs.get('genre_ids')#movie, genres의 id값과 대칭시켜 키값 가져오기


genn=[]
# print(genid,'genid')
# print (genid)
# for i in list(gens):
#     if list(i["id"]) in genid:    
#          print('i')
# (list(m['address'] for m in members)) 리스트에서 딕셔너리 가져오는법
# print (genid)
for i in list(gens): # i는 리스트 gens의 값을 나열한 것이다.
    for k in i.values(): #gens 리스트의 밸류 값은 k이다 k를 순환시켜라
        if k in genid : # k가 genid의 값과 같으면 genn리스트에 i의 키값쌍을 더해라
           genn.append(i.get('name'))
        # print(k,'k')
            # genn = {'name' : i.get('name')}
            # genn.setdefault(f'{k}',str(i.values()))
            # k.get('name')
            # genn.append(i.items())

# print(genn,type(genn))
#리스트 genn의 값 [dict_items([('id', 80), ('name', 'Crime')]), dict_items([('id', 18), ('name', 'Drama')])] <class 'list'>
#리스트에 들어간 name값을 따로 어떻게 찾지?  genn을 딕셔너리로 만드는게 빠를거같다. update를 사용해보자. ua
# update를 사용했더니 키값을 덮어써서 하나의 값만 나온다. #setdefault를 사용해보자, 이것도 이상하게 묶임
#그러면 name 키를 사용해서 값만 가져오면 되니 값만 가져오는걸 생각해보자 genn을 리스트로 바꾸고 append를 사용해서 'name'만 가져오니 됬다.



r = { 'genre_names': genn,
       'id' : movs.get('id'),
      'overview': movs.get ('overview'),
      'title': movs.get('title'),
      'vote_average': movs.get('vote_average'),
      } 
pprint(r) # genre_names가 하나만 나올까? -> update는 덮어쓰기
 # setefault는 키와 값을 새로 묶는거라 기존의 키값을 대입해서 넣으면 통으로 묶여서 제대로 포함이 안된다.
 # genn을 리스트로 만들고 키값을 append와 get ['']을  사용해 name의 값만 넣어서 만들었더니 성공 ㅠㅠ 
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))