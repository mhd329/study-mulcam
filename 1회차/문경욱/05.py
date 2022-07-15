import json
from pprint import pprint


def movie_info(movie, genres):
    info_dict = {}
    genres_name = genres_list[0] #리스트 {'id': 28, 'name': 'Action'} -> 딕셔너리 id : 28 name:Action 으로 바꿔야함.
    
    # for i in genres_list[0]:
    #     print(i) # id와 name만 나옴.
    for i in genres_name:
        print(i)
    
    
    
    
    





    
    movie_ids = movie['genre_ids'] 
    movie_id = movie['id']
    movie_overview = movie['overview']
    movie_title = movie['title']
    movie_average = movie['vote_average']
 
    info_dict['genre_ids'] = movie_ids
    info_dict['id'] = movie_id
    info_dict['overview'] = movie_overview
    info_dict['title'] = movie_title
    info_dict['vote_average'] = movie_average

    #return genres_list #genres_list 출력 확인
    #return type(genres_list) #type : list()
    #return movie_ids
    return genres_name






    #return info_dict #최종 출력
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))