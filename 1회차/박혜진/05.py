import json
from pprint import pprint


def movie_info(movie, genres):
    # print(movie, genres)
    pass 
    # 여기에 코드를 작성합니다.  

    genres_name_list = []
    for i in genres_list :
        for a in movie.get('genre_ids') :
            if i['id'] == a :
                genres_name_list.append(i['name'])
    # print(genres_name_list)

    movie_dic = {
    'genre_names' : genres_name_list,
    'id': movie.get('id'),
    'overview' : movie.get('overview'),
    'title': movie.get('title'),
    'vote_average' : movie.get('vote_average'),
    }

    # pprint(movie_dic)
    return movie_dic


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))