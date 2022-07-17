import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다. 
    result2 = []   
    for movie in movies : 
        gnames = [] 
        for num in movie.get('genre_ids'):
            for i in genres:
                if num == i.get('id'):
                    gnames.append(i.get('name'))

        result = {
            'id' : movie.get('id'),
            'title' : movie.get('title'),
            'vote_average' : movie.get('vote_average'),
            'overview' : movie.get('overview'),
            'genre_names' : gnames
            }
        result2.append(result)
    return result2


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))