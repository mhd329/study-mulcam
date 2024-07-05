import json
from pprint import pprint


def movie_info(movies, genres):
    list = ['id','title', 'vote_average', 'overview']
    result_list = []
    for n in movies:
        result = { "genre_names":[] }
        for i in genres:
            if (i['id'] in n['genre_ids']):
                result["genre_names"].append(i['name'])
        
        for i in n:
            if i in list:
                result[i] = n[i]
        result_list.append(result)
        
    return result_list        
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
    
 