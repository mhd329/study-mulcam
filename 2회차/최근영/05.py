import json
from pprint import pprint


def movie_info(movie, genres_list):
    
    new_genres_list=find_geners(movie.get('genre_ids'),genres_list)
    answer = {
        'genre_names' : new_genres_list,
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    return answer

def find_geners(movie,genres_li):
    re_list=[]
    for i in range(0, len(movie)):
        for j in genres_li:
            if j['id'] == movie[i]:
                re_list.append(j['name'])
    return re_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))