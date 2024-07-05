import json
from pprint import pprint


def movie_info(movie, genres):
     # 여기에 코드를 작성합니다. 
    name = [] #name값 리스트,
    for m in movie['genre_ids']:    #genre_ids=[18,80]
        for genre in genres : #genres 에서
            if genre['id'] == m :  #movie의 genres_ids와 같은 게 있으면
                name.append(genre['name'])  #리스트에 추가

    
    result = {
        'genre_names': name,
        'id': movie.get('id'),
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


    # 삼중for문