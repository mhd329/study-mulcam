import json
from pprint import pprint

# - genre_names는 각 장르 정보를 값으로 가집니다.
# - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

def movie_info(movie, genres):
    

    genre = []
    for x in movie['genre_ids'] :
        
        for y in range(len(genres)) :
            if genres[y]['id'] == x :
                genre += [genres[y]['name']]
                
    
    result = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : genre
    }
    
    return result
          

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))