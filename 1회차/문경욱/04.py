import json
from pprint import pprint


def movie_info(movie):
    movie_ids = movie['genre_ids']
    movie_id = movie['id']
    movie_overview = movie['overview']
    movie_title = movie['title']
    movie_average = movie['vote_average']



    info_dict = {}
    info_dict['genre_ids'] = movie_ids
    info_dict['id'] = movie_id
    info_dict['overview'] = movie_overview
    info_dict['title'] = movie_title
    info_dict['vote_average'] = movie_average

    return info_dict




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))