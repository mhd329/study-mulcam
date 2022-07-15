import json
from pprint import pprint


def movie_info(movies, genres):
    for i in range(len(movies)):
        del movies[i]["adult"]
        del movies[i]["backdrop_path"]
        del movies[i]["original_language"]
        del movies[i]["original_title"]
        del movies[i]["popularity"]
        del movies[i]["poster_path"]
        del movies[i]["release_date"]
        del movies[i]["video"]
        del movies[i]["vote_count"]
        movies[i]["genre_names"]=[]
        for j in range(len(movies[i]["genre_ids"])):
            for k in range(len(genres)): 
                if movies[i]["genre_ids"][j]==genres[k]["id"]:
                    movies[i]["genre_names"].append(genres[k]["name"])
        del movies[i]["genre_ids"]


    return movies  
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))