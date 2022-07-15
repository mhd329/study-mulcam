import json
from pprint import pprint

#[18,]
def movie_info(movie, genres):
    g_list = movie['genre_ids']
    g_name=[] 
    for i in range(len(genres_list)):
        if genres_list[i]['id'] in g_list:
            g_name.append(  genres_list[i]['name']   )

    
    result04 = {'id':movie['id'],'title':movie['title'],'vote_average':movie['vote_average'], 'overview':movie['overview'] ,'genre_name':g_name}

    return result04
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))