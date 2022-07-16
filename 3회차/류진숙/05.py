import json
from pprint import pprint


# genre_ids 안의 인덱스 genre_ids[0] : 18 일때
# 반복문인 genres 안의 genre들을 돌때 18이랑 genre의 id가 같으면
# 리스트 []에 genre['name']의 value값을 집어넣는다 즉 Drama 
def movie_info(movie, genres):
    name = []
    for mv in movie["genre_ids"]:
        for genre in genres:
            if genre["id"] == mv:
                name.append(genre["name"])  
    
    result = {
        "genre_names": name,
        "id": movie.get("id"), 
        "title": movie.get("title"),
        "overview": movie.get("overview"),
        "title": movie.get("title"),
        "vote_average": movie.get("vote_average")
    }

    print(result)
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))