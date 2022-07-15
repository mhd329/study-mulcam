# - 영화 데이터 `movie.json` 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
#     - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
#     - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.
# - `id`, `title`, `vote_average`, `overview`, `genre_ids`으로 구성된 결과를 만듭니다. 
# **(결과 예시 참고)**
# {'genre_ids': [18, 80],
#  'id': 278,
#  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
#              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
#              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
#              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
#              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
#  'title': '쇼생크 탈출',
#  'vote_average': 8.7}

import encodings
import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.
  
    result = {
        'genre_ids' : movie.get('genre_ids'),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
        }
    pprint(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))