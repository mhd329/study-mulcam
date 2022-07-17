import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.
    key_list = ['genre_ids', 'id', 'overview', 'title', 'vote_average']
    movie_info_dict = {}
    for key in key_list:
        movie_info_dict[key] = movie[key]
    return movie_info_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))