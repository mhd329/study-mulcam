import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.
    result = []

    req = "id, title, vote_average, overview, genre_ids".split(", ")
    target = "genre_ids"
    repl = "genre_names"

    for movie in movies:
        data = {i:movie[i] for i in req if i != target}
        data[repl] = [j["name"] for i in movie[target] for j in genres if j["id"] == i]
        result.append(data)

    result = sorted(result, key=lambda x: x["vote_average"], reverse=True)

    return result
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))