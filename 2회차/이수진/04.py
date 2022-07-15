import json
from pprint import pprint


def movie_info(movie):
    del movie["adult"]
    del movie["backdrop_path"]
    del movie["original_language"]
    del movie["original_title"]
    del movie["popularity"]
    del movie["poster_path"]
    del movie["release_date"]
    del movie["video"]
    del movie["vote_count"]

    return movie


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))