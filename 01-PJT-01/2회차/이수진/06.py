import json
from pprint import pprint


def movie_info1(movies, genres):
    unness_info=["adult","backdrop_path","original_language","original_title","popularity","poster_path","release_date","video","vote_count"]
    for i in range(len(movies)):
        for j in unness_info:
            del movies[i][j]
        movies[i]["genre_names"]=[]
        for j in range(len(movies[i]["genre_ids"])):
            for k in range(len(genres)): 
                if movies[i]["genre_ids"][j]==genres[k]["id"]:
                    movies[i]["genre_names"].append(genres[k]["name"])
        del movies[i]["genre_ids"]


    return movies   

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))