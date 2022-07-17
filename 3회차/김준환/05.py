import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.   
    lst = []
    for i in movie.get('genre_ids'):
        for n in range(len(genres)):
            if genres[n]['id'] == i:
                lst.append(genres[n]['name'])
    result = {
        'genre_names' : lst,
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
    }

    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))