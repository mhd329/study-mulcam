import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
    #id, title, vote_average, overview, genre_ids
    with open('./data/movie.json','r', encoding='utf-8')as f:
        json_data = json.load(f)
        result = {
            'genre_ids' : json_data.get('genre_ids'),
            'id' : json_data.get('id'),
            'overview' : json_data.get('overview'),
            'title' : json_data.get('title'),
            'vote_average' : json_data.get('vote_average')
        }
        return pprint(result)
    # return은 딕셔너리로
     
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))