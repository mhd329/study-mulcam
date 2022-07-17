# 프로젝트 01 - 파이썬 기반 데이터 활용
00.py

# 00. 파일에 내용 적기
# with ~ as 키워드를 활용해서 file을 열어 쓰고 읽는 작업 수행


with open('00.txt','w',encoding = 'utf-8') as f:
    f.write('3회차 최태진\n')
    f.write('Hello, Python!\n')
    for char in range(1,6):
        f.write(f'{char}일자 파이썬 공부 중\n')
    
with open('00.txt','r',encoding = 'utf-8') as f:
    print(f.read())

01.py

#파일에 있는 문자열 개수 찾기
#파일을 열고 1줄마다 cnt 1증가
#총 갯수 출력
cnt = 0
with open('fruits.txt','r', encoding = 'utf-8') as f:
    for line in f:  #i가 f에 저장된 데이터를 줄 단위로 읽어옴
        cnt += 1
    print(cnt)
	
02.py

#파일의 데이터를 줄 단위로 읽음
#공백이 있는 경우, .split으로 구분하여 
# 각 인덱스에 해당 단어가 있는지 확인

#find(찾을문자, 찾기시작할위치)
#중복
cnt = 0
t_list = []
with open('fruits.txt','r',encoding = 'utf-8') as f:
    for line in f:
        if line.find('berry') != -1 : #문자열에 berry가 포함되어있다면
            line = line.rstrip()
            if line == 'berryfake':
                continue
            if line not in t_list: 
                t_list.append(line)
                cnt += 1

print(cnt)
print(t_list)
with open('02.txt','w', encoding = 'utf-8') as f:
    f.write(f'{len(t_list)}\n')
    for char in t_list :
        f.write(f'{char}\n')

03.py

#파일 내 데이터 개수
# for문을 활용, 데이터를 라인별로 읽으며 '\n'은 rstrip() method를 통해 제거
# dict에 없는 값이라면 키를 추가하고 값을 1로 설정
# 있다면 값만 +1

dict = {}
with open('fruits.txt','r',encoding = 'utf-8') as f:
    for line in f:
        line = line.rstrip() 
        if line not in dict.keys() :
            dict[line] = 1 
        else:
            dict[line] += 1

print(dict)

with open('03.txt','w',encoding = 'utf-8') as f:
    for i in dict:
        f.write(f'{i} : {dict[i]}\n')

04.py

import json
from pprint import pprint



def movie_info(movie):
    #load() : json문자열을 파이썬 객체로 변환 
    #출력할 내용을 dict에 직접 입력 후 return
    dict = {
        'genre_ids' : movie.get('genre_ids'),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')

    }
    return dict
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))

05.py

import json
from pprint import pprint

#반복문을 통해 movie.json내 "genre_ids"값을 읽어 이 값과
# geners.json파일 내 id값이 일치하는 곳을 찾은 뒤 'name'의 값을 list에 저장


def movie_info(movie, genres):
    tlist = []
    dict = {
        'genre_names' : tlist,
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')

    }
    
    
    
    for i in movie['genre_ids'] :
        # print(i)
        for j in genres :
            if j['id'] == i:
                tlist.append(j.get('name'))
    # print(tlist)
    return dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

## 후기& 느낀점

막연하게 알고있었던 리스트, 딕셔너리 개념을 확실하게 잡는 계기가 되었고, 파일을 통해 읽고 쓰며 약간의 응용으로 json을 python객체로 
로 활용가능하다는 점을 배움.
이번 프로젝트를 통해 코드를 짜기 전, 무엇을 해야하고 큰 덩어리를 작게 나눠 하나씩 해결해 나가는 방법을 배움.
 