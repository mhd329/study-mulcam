import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    my_movie = []

    for movie in movies:
        ids= movie['genre_ids']
        l = []
        for i in ids:
            for j in genres:
                if i == j['id']:
                    l.append(j['name'])
        names = { 'genre_names' : l }

        movie.update(names)

        m = {
            'genre_names': movie.get('genre_names'),
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average')
        }
        my_movie.append(m)
    return(my_movie)
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))