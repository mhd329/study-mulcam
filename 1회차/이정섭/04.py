import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    

    my_dict = {
        'genre_ids': movie['genre_ids'],
        'id' : movie['id'],
        'overview' : movie['overview'],
        'title' : movie['title'],
        'vote_average' : movie['vote_average']        
        }
    return my_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))