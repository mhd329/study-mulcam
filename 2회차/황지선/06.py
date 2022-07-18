# - 영화 데이터 `movies.json` 와 `genres.json` 을  활용하여 필요한 정보로만 구성된 리스트를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 리스트를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.  **(결과 예시 참고)**
#     - 개별 영화 데이터는 `id`, `title`, `vote_average`, `overview`, `genre_names`로 구성된 딕셔너리입니다.
#         - genre_names는 각 장르 정보를 값으로 가집니다.
#         - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

# **TIP. 이전 단계의 코드를 활용할 수 있습니다.**


import json
from pprint import pprint

# 6번은 삼중 포문
# 5번을 여러개 넣은 리스트라고 생각해도 됨
# for문 하나만 써도 된대!!!!!!!!!!!!!!!!
# 5번코드를 풀어서 복붙해서~ for문을 잘 넣으면 됨!


def movie_info(movies, genres):
    mov = []
    for m in movies:
        names = []
        for i in m['genre_ids']:
            for j in genres:
                if i == j['id']:
                    names.append(j['name'])

        result = {'genre_names': names,
                'id': m.get('id'),
                'overview': m.get('overview'),
                'titile': m.get('title'),
                'vote_average': m.get('vote_average')}
        mov.append(result)
    return mov


# def movie_info(movies, genres):

#     def movie_return():
#         names = []
#         for m in range(len(movies)):
#             for n in movies[m].get('genre_ids'):
#                 for i in range(len(genres)):
#                     if n == genres[i].get('id'):
#                         names.append(genres[i].get('name'))

#         # for m in range(len(movies)):
#         #     for n in range(len(movies[m].get('genre_ids'))):
#         #         for g in range(len(genres)):
#         #             if movies[m].get('genre_ids') == genres[g].get('id'):
#         #                 names.append(genres[g].get('name'))
#         return names

#     result = []
#     for i in range(len(movies)):
#         result.append({
#             'id' : movies[i].get('id'),
#             'title' : movies[i].get('title'),
#             'vote_average' : movies[i].get('vote_average'),
#             'overview' : movies[i].get('overview'),
#             'genre_names' : movie_return()
#         })
        
#     return result 
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    
    pprint(movie_info(movies_list, genres_list))



#     [{'genre_names': ['Drama', 'Crime'],
#   'id': 278,
#   'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '    
#               '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '    
#               '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '   
#               '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
#               '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
#   'title': '쇼생크 탈출',
#   'vote_average': 8.7},
#  {'genre_names': ['Drama', 'Crime'],
#   'id': 238,
#   'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '
#               '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '
#               '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '
#               '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 '
#               '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 '
#               '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.',
#   'title': '대부',
#   'vote_average': 8.7},
#  {'genre_names': ['Drama', 'History', 'War'],
#   'id': 424,
#   'overview': '2차 세계대전 당시 독일군이 점령한 폴란드. 시류에 맞춰 자신의 성공을 추구하는 기회주의자 쉰들러는 유태인이 '
#               '경영하는 그릇 공장을 인수한다. 그는 공장을 인수하기 위해 나찌 당원이 되고 독일군에게 뇌물을 바치는 등 갖은 '
#               '방법을 동원한다. 그러나 냉혹한 기회주의자였던 쉰들러는 유태인 회계사인 스턴과 친분을 맺으면서 냉혹한 유태인 '
#               '학살에 대한 양심의 소리를 듣기 시작한다. 마침내 그는 강제 수용소로 끌려가 죽음을 맞게될 유태인들을 구해내기로 '
#               '결심하고, 독일군 장교에게 빼내는 사람 숫자대로 뇌물을 주는 방법으로 유태인들을 구해내려는 계획을 세우는데...',
#   'title': '쉰들러 리스트',
#   'vote_average': 8.6},
# ...