import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다. 
    req = "id, title, vote_average, overview, genre_ids".split(", ")
    target = "genre_ids"
    repl = "genre_names"
    data = {i:movie[i] for i in req if i != target}
    data[repl] = [j["name"] for i in movie[target] for j in genres if j["id"] == i]

    return data

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))