import json
from pprint import pprint
from re import A


def movie_info(movies, genres):
    result =[]
    
    for dics in range(len(movies)) :
        result.append({})                 
        for i in movies[dics] : 
            if i == 'id' or i == 'title'or i =='vote_average'or i == 'overview' or i == 'genre_ids' :
                result[dics][i] = movies[dics][i]         ##movies[dics] -> 딕셔너리
        for i in movies[dics] :
            if i == 'genre_ids' :
                result[dics]['genre_names']= []
                for j in result[dics][i] :
                    for k in range(len(genres)) :
                        if j == genres[k]['id'] :
                            result[dics]['genre_names'].append(genres[k]['name'])
                result[dics].pop(i)     
        
            
    return result
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))



   
               