import json
from pprint import pprint


def movie_info(movie):
    movie2 = {}
    movie2['genre_ids'] = movie['genre_ids']
    movie2['id'] = movie['id']
    movie2['overview'] = movie['overview']
    movie2['title'] = movie['title']
    movie2['vote_average'] = movie['vote_average']
    return movie2

    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))