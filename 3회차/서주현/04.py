import json
from pprint import pprint


def movie_info(movie):
    a = {}
    for i in movie :
        if i == 'id' or i == 'title'or i =='vote_average'or i == 'overview' or i == 'genre_ids' :
            a[i] = movie[i]
        
    
                        
    return a

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))





    #  a[i] = []
    #             a[i] ='fffffff'
    #             for j in movie[i] :            # movie(genre)
    #                for k in movie[i][j] :          # movie[genre][id]
    #                     if k == 'id' :
    #                         a['genre_ids'] = movie[i][j][k]  
    #                         print(1)    