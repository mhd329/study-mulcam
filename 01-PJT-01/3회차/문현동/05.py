import json
from pprint import pprint

def movie_info(movie, genres):
    
    res =\
    {
        'genre_names': [],
        'id' : movie['id'],
        'overview' : movie['overview'],
        'title' : movie['title'],
        'vote_average' : movie['vote_average']
    }
    
    genre_ids = []
    
    genre_ids += movie['genre_ids']

    for i in genres_list:
        for j in genre_ids:
            if i['id'] == j:
                res['genre_names'].append(i['name'])
                genre_ids.remove(j)
                
    return res
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))