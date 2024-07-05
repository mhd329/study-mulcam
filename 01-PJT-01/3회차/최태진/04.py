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