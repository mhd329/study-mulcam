import json
from pprint import pprint

# 'movies.json', 'genres.json' 파일을 불러와 필요한 정보로만 구성된 리스트 출력
def movie_info(movies, genres):
    movies_info = []
    for movie in movies:
        # 각 영화별 정보 초기화
        movie_info = {
            'id': movie.get('id'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average'),
            'overview': movie.get('overview'),
            'genre_names':[]
        }

        # genre_ids에 해당하는 genre_names 설정
        for id in movie.get('genre_ids'):
            for genre in genres:
                if genre.get('id') == id:
                    movie_info['genre_names'].append(genre.get('name'))
                    break
        
        # movies_info 변수에 현재 한 영화의 정보를 추가
        movies_info.append(movie_info)
    
    return movies_info


        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))