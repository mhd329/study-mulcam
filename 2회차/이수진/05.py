import json
from pprint import pprint


def movie_info(movie, genres):
    del movie["adult"]
    del movie["backdrop_path"]
    del movie["original_language"]
    del movie["original_title"]
    del movie["popularity"]
    del movie["poster_path"]
    del movie["release_date"]
    del movie["video"]
    del movie["vote_count"]
    for i in range(len(genres)):
        if genres[i]["id"]==movie["genre_ids"][0]:
            movie["genre_ids"][0]=genres[i]["name"]
        elif genres[i]["id"]==movie["genre_ids"][1]:
            movie["genre_ids"][1]=genres[i]["name"]


    return movie  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))