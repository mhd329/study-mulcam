import json
from pprint import pprint


def movie_info(movie, genres):
    
    genres_name = [] # genres_name 이라는 저장소를 만듬
    for id in movie.get('genre_ids'): # movie_json 파일에서 genre_ids 가져온 후 id에 입력
        for name in genres: # genres_json 파일에서 id와 name 가져온 후 name 함수에 입력
            if id == name.get('id'): # if  movie_json 파일의 id 와 genres_ids의 'id'가 같은지
                genres_name.append(name.get('name')) # 같다면 genres_name 저장소에 genres_json 파일에서 가져온 'name' append

    result = {
        'id': movie.get('id'), #  movie.json 딕셔너리 파일에서 id를 가져옴
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_names': genres_name # append된 genres_name 출력
        }
    
    return result # result를 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))