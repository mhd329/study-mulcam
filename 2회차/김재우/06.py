import json
from pprint import pprint


def movie_info(movies, genres):
    
    movie_all = [] # 모든 영화의 내용을 저장할 저장소
    
    for movie in movies: #movies라는 movies.json 파일을 movie라는 임시공간에 넣음
        genres_name = []
        for id in movie.get('genre_ids'): # movie라는 공간에서 genre_ids 가져온 후 id에 입력
            for name in genres: # genres_json 파일에서 id와 name 가져온 후 name 함수에 입력
                if id == name.get('id'): # if  movie_json 파일의 id 와 genres_ids의 'id'가 같은지
                    genres_name.append(name.get('name')) # 같다면 genres_name 저장소에 genres_json 파일에서 가져온 'name' append

        result = {
            'id': movie.get('id'), #  movie 공간에서 id를 가져옴
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average'),
            'overview': movie.get('overview'),
            'genre_names': genres_name 
        }
        
        movie_all.append(result) # movie_all에 result 결과를 append(추가)
    
    return movie_all # movie_all 내보내줌

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))