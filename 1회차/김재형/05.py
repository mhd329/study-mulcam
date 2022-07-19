import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    def genres_name():
        genres_name = []
        for gen_id in movie['genre_ids']:
            # print(gen_id)
            for gen_num in genres:
                # print(gen_num.get("id"))
                if gen_id == gen_num.get("id"):
                    genres_name.append(gen_num.get("name"))
        return genres_name
    result = {
        'genre_names' : genres_name(),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    return result
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))