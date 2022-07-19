import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    m = open('./data/movie.json', 'r', encoding='utf-8')
    o = json.load(m)
    g = open('./data/genres.json', 'r', encoding='utf-8')
    e = json.load(g)
    g_l = []

    for a in o.get('genre_ids'):
        for i in e:
            if a == i.get('id'):
                g_l.append(i['name'])
            
    result = {
        'genre_names' : g_l,
        'id' : o.get('id'),
        'overview' : o.get('overview'),
        'title' : o.get ('title'),
        'vote_average' : o.get('vote_average')}
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))