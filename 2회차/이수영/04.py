import json
from pprint import pprint


def movie_info(movie):
    result = {'gener_ids' : movie.get('gener_ids'),
              'id' : movie.get('id'),
              'overview' : movie.get('overview'),
              'teitle' : movie.get('titel'),
              'vote_average' : 8.7}
    return result   
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))