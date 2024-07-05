import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    rresult = []
    for k in movies:
        gnames = []
        for i in k['genre_ids']:
            for j in genres:
                if i == j['id']:
                    gnames.append(j['name'])

        result = {'genre_names': gnames,
                'id': k.get('id'),
                'overview': k.get('overview'),
                'titile': k.get('title'),
                'vote_average': k.get('vote_average')}
        rresult.append(result)
    return rresult
    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))