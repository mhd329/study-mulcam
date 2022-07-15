import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    movie_genre_ids = movie.get('genre_ids')
    movie_genre_names = []
    
    for mgi in movie_genre_ids:
        for genre in genres:
            if mgi == genre.get('id'):
                movie_genre_names.append(genre.get('name'))
                
    result = {
        'genre_ids': movie_genre_names,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'poster_path': movie.get('poster_path'),
        'title': movie.get('title'),
        'vote_average':movie.get('vote_average')
    }
    
    return result    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))