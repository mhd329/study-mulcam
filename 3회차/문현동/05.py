import json
from pprint import pprint

def movie_info(movie, genres):
    
    genre_ids_list = []
    for i in range(len(movie['genre_ids'])):
        genre_ids_list.append(movie['genre_ids'][i])
    
    res =\
    {
        'genre_names': genre_ids_list,
        'id' : movie['id'],
        'overview' : movie['overview'],
        'title' : movie['title'],
        'vote_average' : movie['vote_average']
    }
    
    return res
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))