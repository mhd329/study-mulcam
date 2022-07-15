import json
from pprint import pprint


def movie_info():
    pass 
    # 여기에 코드를 작성합니다.  
    movie_json = open('/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('/Users/imac01/Desktop/multicampus/01-PJT-01/3회차/김태형/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)
    
    movie_genre = []
    for i in genres_list:
        for j in movie['genre_ids']:
            if i['id']==j:
                movie_genre.append(i['name'])
    movie_dict = {}
    movie_dict['genre']=movie_genre
    movie_dict['id']=movie['id']
    movie_dict['overview']=movie['overview']
    movie_dict['title']=movie['title']
    movie_dict['vote_average']=movie['vote_average']
    pprint(movie_dict)        

movie_info()
# 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     movie_json = open('data/movie.json', encoding='UTF8')
#     movie = json.load(movie_json)

#     genres_json = open('data/genres.json', encoding='UTF8')
#     genres_list = json.load(genres_json)

#     pprint(movie_info(movie, genres_list))