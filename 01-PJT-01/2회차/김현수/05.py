import json
from pprint import pprint
a = []
#count = 0

def movie_info(movie, genres):
    #print(type(movie.get('genre_ids'))) 리스트로 받았음
    for id in movie.get('genre_ids'):
        for dict in genres:
            if dict['id'] == id: #id값에 따른 영화이름 가져오기
                #print(dict['name'],type(dict['name']))  #dict['name']은 string
                a.append(dict['name'])

    return {'genre_names' : a,
    'id': movie.get('id'),
    'overview': movie.get('overview'),
    'title': movie.get('title'),
    'vote_average': movie.get('vote_average')
    }
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))