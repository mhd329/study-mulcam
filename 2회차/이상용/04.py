# 영화 데이터 movie.json 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오. 
# id, title, vote_average, overview, genre_ids으로 구성된 결과를 만듭니다. 

import json
from pprint import pprint

def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
    result = {'genre_ids': movie.get('genre_ids'),
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average')}
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))