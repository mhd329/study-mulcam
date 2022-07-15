import json
from pprint import pprint


def movie_info(movies, genres):

    final_result = []


    for mov in movies:
        for num in mov.get('genre_ids'):
            for i in genres:
                if num == i.get('id'):
                    genres_names = []
                    genres_names.append(i.get('name'))

            result = {
                'id' : mov.get('id'),
                'title' : mov.get('title'),
                'vote_average' : mov.get('vote_average'),
                'overview' : mov.get('overview'),
                'genre_names' : genres_names,
            }

            final_result.append(result)

    return final_result
#     # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))