import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    f_movie = open('data/movie.json', 'r', encoding='utf-8')    
    f_genres = open('data/genres.json', 'r', encoding = 'utf-8')
    mv = json.load(f_movie)
    gr = json.load(f_genres)
    lst = []
    for i in mv.get('genre_ids'):
        for n in range(len(gr)):
            if gr[n]['id'] == i:
                lst.append(gr[n]['name'])
    result = {
        'genre_names' : lst,
        'id' : mv.get('id'),
        'title' : mv.get('title'),
        'vote_average' : mv.get('vote_average'),
        'overview' : mv.get('overview'),
    }

    pprint(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))