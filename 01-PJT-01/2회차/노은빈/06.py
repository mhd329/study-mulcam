import json
from pprint import pprint


def movie_info(movies, genres): 
    # 여기에 코드를 작성합니다. 
    movie_list = []  #영화리스트
    for movie in movies :
        genre_name = [] #영화 리스트,    
        for mv in movie['genre_ids']:    #genre_ids=[18,80]
            for genre in genres : #genres 에서
                if genre['id'] == mv :  #movie의 genres_ids와 같은 게 있으면
                    genre_name .append(genre['name'])  #리스트에 추가

    
    result = {
        'genre_names': genre_name,
        'id': movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        
    }
    movie_list.append(result)
    return movie_list    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

    #5번 코드 그대로 붙여넣기 한 담에 이어서 코드 작성