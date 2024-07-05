import json
from pprint import pprint


def movie_info(movies, genres):
    
    new_list = []
    for movie in movies:
        mov_list = []
        for a in genres_list:
            if a.get('id') in movie.get('genre_ids'):
                mov_list.append(a.get('name'))
            
                result = {
        'genre_names' :mov_list,
        'id' : movie.get('id'),
        "overview" : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' :movie.get('vote_average')
        }
        new_list.append(result)
    return new_list
    
    

    # mov_list = {}
    # new_list = []
    # for b in movies_list:
    #   for a in genres_list:  
    #     if  a.get('id') in b.get('genre_ids'):
    #       mov_list ={'genre_names' : a.get('name'),
    #     'id' : b.get('id'),
    #     'overview' : b.get('overview'),
    #     'title' : b.get('title'),
    #     'vote_average' :b.get('vote_average')
    #         }
    #     print(mov_list)
        
            

    # for a in movies_list:
    #     result = {
    #     'genre_names' : a.get('id'),
    #     'id' : a.get('id'),
    #     'overview' : a.get('overview'),
    #     'title' : a.get('title'),
    #     'vote_average' :a.get('vote_average')
    #     }


   
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))