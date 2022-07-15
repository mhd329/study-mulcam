import json
from pprint import pprint
from unittest import result


def movie_info(movies, genres):
    result = []
    # 장르는 id 와 name
    # 장르의 id와 list의 genre_ids가 같으면 장르의 name을 temp가 받아온다.
    
    for list in movies:
        temp = {}
        gen_list = []

        for idx in range(0, len(list['genre_ids'])):
            for gen in genres:
                if gen['id'] == list['genre_ids'][idx]:
                    gen_list.append(gen['name'])
        
        temp['genre_names'] = gen_list

        temp['id'] = list['id']
        
        temp['title'] = list['title']

        temp['vote_average'] = list['vote_average']

        temp['overview'] = list['overview']

        result.append(temp)

    return result
    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))