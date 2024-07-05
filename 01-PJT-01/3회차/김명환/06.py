import json
from pprint import pprint


def movie_info(movies, genres):
    f1= open('data\\movies.json','r',encoding = 'utf-8')
    movies =  json.load(f1)
    genre_names=list()
    f2= open('data\\genres.json','r',encoding = 'utf-8')
    genres =  json.load(f2)
     
    for movie in movies: 
        for i in range(len((movie['genre_ids']))): #2 0,1
            for j in range(len(genres)):
                if movie['genre_ids'][i] == genres[j]['id']:
                    genre_names.append(genres[j]['name'])
        movie['genre_names'] = genre_names
   
    result = {
        'genre_names' : movies.get('genre_names'),
        'genre_ids' : movies.get('genre_id'),
        'id' : movies.get('id'),
        'overview' : movies.get('overview'),
        'title' : movies.get('title'),
        'vote_average' : movies.get('vote_average')
    }
    pprint (result)            
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))