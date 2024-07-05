import json
from pprint import pprint


def movie_info(movies, genres):
    
    movies_review = []
    
    for movie in movies:
        genre_name = []
        genre_ids = movie['genre_ids'] 


        for genre in genres:
            if genre['id'] in genre_ids:
                genre_name.append(genre['name'])
            

        key_list = ['id','title','vote_average','overview']
        movie_info_dict = {}

        for key in key_list:
            movie_info_dict[key] = movie[key]
        
        movie_info_dict['gerne_names'] = genre_name
        movies_review.append(movie_info_dict)
    
    return movies_review

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('2회차/2회차-이호빈/이호빈/data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('2회차/2회차-이호빈/이호빈/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))