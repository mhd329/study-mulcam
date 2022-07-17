# 영화 데이터 `movie.json` 와 `genres.json` 을  활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
# 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
# JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# `id`, `title,` `vote_average`, `overview`, `genre_names`로 결과를 만듭니다.
# genre_names는 각 장르 정보를 값으로 가집니다.
# genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.


import json
from pprint import pprint

def movie_info(movie, genres): # movie_info 라는 함수를 만들 건데
    names = [] # 일단 장르 이름을 넣기 위한 리스트를 만들고
    for number in movie['genre_ids']: # movie.json 안에 있는, 'genre_ids'라는 키와 짝인 밸류(==[18, 20])의 변수(==number)에 대해 반복할 건데
        for i in range(len(genres)): # 또, 0부터 genres.json 안에 있는 딕셔너리들의 크기까지의 범위(==0~18)의 변수(==i)에 대해서도 반복을 할 건데 (너무 길다)
            if genres[i]['id'] == number: # 만약에 [i]['id']('다중 리스트' 구글링 해서 참고할 것)가 number와 일치할 경우
                names.append(genres[i]['name']) # names 리스트에 [i]['name']를 추가해서 names 리스트를 다 만들고
        
    result = { # result라는 딕셔너리를 만든 다음
    'genre_names' : names, # 키와 밸류를 불러와서
    'id' : movie['id'],
    'overview' : movie['overview'],
    'title' : movie['title'],
    'vote_average' : movie['vote_average']
    }

    return result # 이 값을 반환함

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))


# output
# {'genre_names': ['Drama', 'Crime'],
#  'id': 278,
#  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을
#  쓴다. 주변의 증언과 살해 현장의 '
#              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은  
# 교도소 쇼생크로 향한다. 인간 말종 '
#              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급
# 을 당한다. 그러던 어느 날, 간수의 '
#              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된
# 다. 그 와중에 교도소 소장은 죄수들을 '
#              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면 
# 서 그의 돈을 관리하는데...',
#  'title': '쇼생크 탈출',
#  'vote_average': 8.7}