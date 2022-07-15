import json
from pprint import pprint


def movie_info(movies, genres):
    
    '''res =\
    {
        'genre_names': genre_ids_list,
        'id' : 0,
        'overview' : '',
        'title' : '',
        'vote_average' : 0
    }
    
    for i in movies:
        genre_ids_list
        res['id'] = movies[i]['id']
        res['overview'] = movies[i]['overview']
        res['title'] = movies[i]['title']
        res['vote_average'] = movies[i]['vote_average']
    
        genre_ids_list = []
        for j in range(len(movies[i]['genre_ids'])):
            genre_ids_list.append(movies[i]['genre_ids'][j])
    
    return res'''
    pass
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))