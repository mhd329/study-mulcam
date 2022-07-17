import json
from pprint import pprint


def movie_info(movie):
    # id, title, vote_average, overview, genre_ids
    result = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'genre_ids' : movie.get('genre_ids')
            }
    print(result)
    return(result)
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))