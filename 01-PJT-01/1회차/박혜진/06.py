import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.

    movies_dict = []
    movies_list_dic = []

    for m in movies :
        
        genres_name_list = []
        
        for i in genres_list :
            for a in m['genre_ids'] :
                if i['id'] == a :
                    genres_name_list.append(i['name'])
        
        # print(genres_name_list)
    

        movie_dic = {
        'genre_names' : genres_name_list,
        'id': m['id'],
        'overview' : m['overview'],
        'title': m['title'],
        'vote_average' : m['vote_average'],
        }

        movies_dict.append(movie_dic)

        # pprint(movies_dict)
    return movies_dict


        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))