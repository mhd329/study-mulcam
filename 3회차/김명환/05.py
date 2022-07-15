import json
from pprint import pprint
from re import M


def movie_info(movie, genres):
    f1= open('data\\movie.json','r',encoding = 'utf-8')
    movie =  json.load(f1)
    genre_names=list()
    f2= open('data\\genres.json','r',encoding = 'utf-8')
    genres =  json.load(f2)
    
    for i in range(len((movie['genre_ids']))): #2 0,1
        for j in range(len(genres)):
            if movie['genre_ids'][i] == genres[j]['id']:
                genre_names.append(genres[j]['name'])
    movie['genre_names']=genre_names
   

    result ={
        'genre_names' : movie.get('genre_names'),
        'genre_ids' : movie.get('genre_id'),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    pprint (result)        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))