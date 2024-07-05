import json
from pprint import pprint


def movie_info(movie, genres):
    pass
    def gen_name():
        gen_name = []
        for m in movie.get('genre_ids'):
            for g in genres_list:
                if m == g.get('id'):
                    gen_name.append(g.get('name'))
        return gen_name
    
    result = {
        'genre_names' : gen_name(),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    
    return result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))