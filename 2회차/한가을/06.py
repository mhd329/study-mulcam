import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    result = []

    for m in movies:
        for n in m.get('genre_ids'):
            for i in genres:
                if n == i.get('id'):
                    genres_names = []
                    genres_names.append(i.get('name'))

            result2 = {
                'id' : m.get('id'),
                'title' : m.get('title'),
                'vote_average' : m.get('vote_average'),
                'overview' : m.get('overview'),
                'genre_names' : genres_names
            }

            result.append(result2)
    
    return result
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))