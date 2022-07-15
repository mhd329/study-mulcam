import json
from pprint import pprint


def movie_info(movie, genres):
   
    f = open('data/movie.json', 'r', encoding = 'utf-8')
    g = json.load(f)
    h = open('data/genres.json', 'r', encoding = 'utf-8')
    i = json.load(h)
    # print(i, type(i))
    genre_group = []
    for genre_name in g.get('genre_ids'):
        for a in i:
            for genre_code in a:
                if genre_name == a[genre_code]:
                    genre_group.append(a['name'])
    
    result = {
        'genre_ids' : genre_group,
        'id' : g.get('id'),
        'overview' : g.get('overview'),
        'title' : g.get('title'),
        'vote_average' : g.get('vote_average')
    }
    pprint(result)
    pass 
    # 여기에 코드를 작성합니다.  
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))