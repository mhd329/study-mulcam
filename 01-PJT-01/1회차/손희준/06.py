import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.
    movies_info_dict = []    
    
    for movie in movies:        
        genre_ids = movie['genre_ids']        
        gerne_names = []        
        for genre in genres:            
            if genre['id'] in genre_ids:                
                gerne_names.append(genre['name'])        
        key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']        
        movie_info_dict = {}        
        for key in key_list:
            movie_info_dict[key] = movie[key]        
        movie_info_dict['gerne_names'] = gerne_names        
        movies_info_dict.append(movie_info_dict)
    return movies_info_dict
    
 

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
    
import sys
sys.stdout = open('06.txt','w',encoding='utf-8')
pprint(movie_info(movies_list, genres_list))