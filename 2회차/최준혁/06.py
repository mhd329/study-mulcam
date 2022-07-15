import json
from pprint import pprint

def movie_info(movies, genres):

    m_result = []
    for all in movies:
        for ids in all.get('genre_ids'): 
            for id in genres:
                if ids == id.get('id'): 
                    g_names = []
                    g_names.append(id.get('name')) 

        result = {
            'genre_names'  : g_names,
            'genre_ids'    : all.get('genre_ids'),
            'overview'     : all.get('overview'),
            'title'        : all.get('title'),
            'vote_average' : all.get('vote_average')
        } 
        m_result.append(result) 
    return m_result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    #movie_info(movies_list, genres_list)
    pprint(movie_info(movies_list, genres_list))



