import json
from pprint import pprint


def movie_info(movies, genres):
    pass 

#id, title, vote_average, overview, genre_names
#id, title, vote_average, overview, genre_names
#- genre_names는 각 장르 정보를 값으로 가집니다.
# - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.
#전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.  

    # 여기에 코드를 작성합니다.  
mo = open('data/movies.json','r',encoding='utf8') 
ge = open('data/genres.json','r',encoding='utf8')
mov = json.load(mo)
gen = json.load(ge)   #리스트 안에 인덱스가 있음
gens = gen
movs = mov
genid =[]
genn=[]
for sequence in range(len(mov)):
    genid = movs[sequence].get('genre_ids')# 
    for i in list(gens): # i는 리스트 gens의 값을 나열한 것이다.
        for k in i.values(): #gens 리스트의 밸류 값은 k이다 k를 순환시켜라
         if k in genid : # k가 genid의 값과 같으면 genn리스트에 i의 키값쌍을 더해라
            genn.append(i.get('name'))
            r = { 'genre_names': genn,
              'id' : movs[sequence].get('id'),
              'overview': movs[sequence].get ('overview'),
             'title': movs[sequence].get('title'),
             'vote_average': movs[sequence].get('vote_average'),
              }         
    pprint(r)
    genn.clear()
             #genre_names를 넣은 리스트가 계속 쌓여서 한번에 나옴 이걸 해결하라면?
             #순서를 잘 생각해보자 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))