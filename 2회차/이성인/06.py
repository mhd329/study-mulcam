import json
from pprint import pprint

# 해야 할것. 무비를 리스트로 만들다. 
# 리스트를 하나하나 result에 적용하고 result를 리스트에 넣는다. 
# 끝
def movie_info(movies, genres):
    genre_names =[]
    result_list = []
    movies_list = list(movies)
    n3 = len(movies_list)
    for i in range(n3):
        genre_names = []
        movies = movies_list[i]
        n = len(genres)
        n2 = len(movies.get('genre_ids'))
        for i in range(n):
            for j in range(n2):
                if genres[i].get('id') == movies.get('genre_ids')[j]:
                    genre_names.append(genres[i].get('name'))
        result = {
            'genre_names' : genre_names,
            'id' : movies.get('id'),
            'overview' : movies.get('overview'),
            'title' : movies.get('title'),
            'vote_average' : movies.get('vote_average'),
        }
        result_list.append(result)
    return result_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))