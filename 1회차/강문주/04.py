import json
from pprint import pprint


def movie_info(movie):
    # 여기에 코드를 작성합니다.
    id = movie['id']
    title = movie['title']
    vote_average = movie['vote_average']
    overview =  movie['overview']
    genre_ids = movie['genre_ids']

    result = { 'genre_ids': genre_ids,'id': id, 'title': title, 'vote_average': vote_average, 
    'overview': overview}
    pprint(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))