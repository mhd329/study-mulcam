import json
from pprint import pprint

# - 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.  **(결과 예시 참고)**
# - 개별 영화 데이터는 `id`, `title`, `vote_average`, `overview`, 
# `genre_names`로 구성된 딕셔너리입니다.
#  - genre_names는 각 장르 정보를 값으로 가집니다.
#  - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

def movie_info(movies, genres):
    
    
    result = {}
    answer = []
    
    for x in range(len(movies)):
        genre = []
        
        for y in movies[x]['genre_ids'] :
            
            for z in range(len(genres)) :
                
                if y == genres[z]['id'] :
                    genre += [genres[z]['name']]
                    
                    result = {
             'id' : movies[x].get('id'),
             'title' : movies[x].get('title'),
             'vote_average' : movies[x].get('vote_average'),
             'overview' : movies[x].get('overview'),
             'genre_names' : genre
            }
                    answer += [result]
    
    return answer
   
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))