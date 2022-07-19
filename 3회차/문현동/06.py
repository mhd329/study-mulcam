import json
from pprint import pprint


def movie_info(movies, genres):
    
    res_list = []
    genre_ids_list = []
    names_list = []
    names = []
    for i in movies:
        genre_ids_list += [i['genre_ids']]

    for i in genre_ids_list: # [18,80] / [18,80] / [18,36,10752]
        for j in i: # 80
            for k in genres_list:
                if j == k['id']:
                    names.append(k['name'])
        names_list.append(names)
        names = []
                    
    for i in movies:
        res_list.append({})
    
    i = 0
    j = 0
    
    while i < len(res_list):
        res_list[j]['genre_names'] = names_list[i]
        res_list[j]['id'] = movies[i]['id']
        res_list[j]['overview'] = movies[i]['overview']
        res_list[j]['title'] = movies[i]['title']
        res_list[j]['vote_average'] = movies[i]['vote_average']
        
        i += 1
        j += 1
            
    return res_list
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))