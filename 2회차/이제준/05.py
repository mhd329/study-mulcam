import json
from pprint import pprint


def movie_info(movie, genres_list):
    list = movie.get('genre_ids')       # list라는 변수를 만든다 (genre_ids의 리스트가 들어가 있음)
    genre_names = []                    
        # genre_names라는 list를 만든다

    for i in list:                      # 'movie.json' 폴더 genre_ids, list에 있는 숫자들을 꺼낸다 (list to int)
        for names in genres_list:       # 'genres.json' 폴더에 있는 리스트들을 하나씩 확인한다
            if names['id'] == i:        # id의 값과 genre_ids 값이 같으면
                genre_names.append(names['name'])   # genre_names의 리스트에 항목을 추가한다

    return{
        'id': movie.get('id'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_names': genre_names
    }
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))