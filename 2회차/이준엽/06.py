import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    result = []
    for movie in movies_list :
        g_name = []
        g_id = movie.get('genre_ids')
        for id in g_id :
            for g_list in genres_list:
                if g_list['id'] == id :
                    g_name.append(g_list.get('name'))
        indimovie = {
            'genre_name': g_name,
            'id': movie.get('id'),
            'overview' : movie.get('overview'),
            'title' : movie.get('title'),
            'vote_average' : movie.get('vote_average')
        }
        result.append(indimovie)
    return result
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))