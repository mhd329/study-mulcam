import json
from pprint import pprint


def movie_info(movie):
    pass 
    for key, value in movie.items():
        print(f'\'{key}\' : \'{value}\'', end=',\n')
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))