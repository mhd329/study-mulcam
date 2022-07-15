import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    def genres_name():
        genres_name = []
        for gen_id in movies['genre_ids']:
            # print(gen_id)
            for gen_num in genres:
                # print(gen_num.get("id"))
                if gen_id == gen_num.get("id"):
                    genres_name.append(gen_num.get("name"))
        return genres_name

    for movie in movies :
        result = {
            'genre_names' : genres_name(),
            'id' : movies.get('id'),
            'title' : movies.get('title'),
            'overview' : movies.get('overview'),
            'vote_average' : movies.get('vote_average')
        }

    return movie
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))