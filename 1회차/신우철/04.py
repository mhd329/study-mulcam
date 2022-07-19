import json
from pprint import pprint


def movie_info(movie):
    movie_data = {}
    movie_data['genre_ids'] = movie['genre_ids']
    movie_data['id'] = movie['id']
    movie_data['overview'] = movie['overview']
    movie_data['title'] = movie['title']
    movie_data['vote_average'] = movie['vote_average']
    return movie_data



    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
    
