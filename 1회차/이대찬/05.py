import json
from pprint import pprint


def movie_info(movie, genres): #리스트
    result = { "genre_names":[] }

    for i in genres:
        if (i['id'] in movie['genre_ids']):
            result["genre_names"].append(i['name'])
        
    list = ['id','title', 'vote_average', 'overview']
    for i in movie:
        if i in list:
            result[i] = movie[i]
        
    return result
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
    
    
