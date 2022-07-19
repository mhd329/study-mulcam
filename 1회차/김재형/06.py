import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.
    movie_list = []
    for mov in movies:
        def genres_name():
            genres_name = []
            for gen_id in mov['genre_ids']:
                for gen_num in genres:
                    if gen_id == gen_num.get("id"):
                        genres_name.append(gen_num.get("name"))
                        
            return genres_name
        result = {
            'genre_names' : genres_name(),
            'id' : mov.get('id'),
            'title' : mov.get('title'),
            'overview' : mov.get('overview'),
            'vote_average' : mov.get('vote_average')
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