import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    my_dict_list=[]
    for m in movies:
        names =[]
        for i in m['genre_ids']:
            for j in range(0, len(genres)):
                if genres[j]['id'] == i:
                    names.append(genres[j]['name'])
        my_dict = {}
        my_dict = {
            'genre_names': names,
            'id' : m['id'],
            'overview' : m['overview'],
            'title' : m['title'],
            'vote_average' : m['vote_average']
            }
        my_dict_list.append(my_dict)

    return my_dict_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))