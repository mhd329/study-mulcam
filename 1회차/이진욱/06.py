import json
from pprint import pprint


def movie_info(movies, genres):
    m_list=[0]*20
    for i in range(20):
        g_list = movies_list[i]['genre_ids']
        g_name=[] 
        for j in range(len(genres_list)):
            if genres_list[j]['id'] in g_list:
                g_name.append(  genres_list[j]['name']   )
        m_list[i]={'id':movies_list[i]['id'],'title':movies_list[i]['title'],'vote_average':movies_list[i]['vote_average'], 'overview':movies_list[i]['overview'] ,'genre_name':g_name}

    return m_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))