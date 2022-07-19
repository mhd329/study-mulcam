import json
from pprint import pprint


def movie_info(movies, genres):
    
    movies_info_dict = [] # 출력할 영화 리스트 
    

    for movie in movies:
        genre_ids = movie['genre_ids']  # 1) 각 무비 장르 id값으로 매치하여 키값을 하나씩 넣어놓고

        genre_names = [] # 각 키를 매치하여 1개이상 장르를 리스트에 넣어둠

        for genre in genres:
            if genre['id'] in genre_ids: # 2) 1번에서 넣어둔 거와 매치하여 id 가 있으면  
                genre_names.append(genre['name']) # 3) name의 키값을 리스트에 넣는다.
       
        movie_info_dict = {}
        movie_info_dict['genre_names'] = genre_names # 장르 네임만 따로 먼저 딕셔너리에 넣어둠
        
        key_list = ['id','title','vote_average','overview']
    
        for key in key_list:
            movie_info_dict[key] = movie[key] 
           
        movies_info_dict.append(movie_info_dict) # 각 키 값을 구성한 영화 하나 완성 후 append 
        
    return movies_info_dict
        
        
# 아래의 코드는 수정하지 않습니다.

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))