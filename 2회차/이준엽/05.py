import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
# 여기에 코드를 작성합니다.  
    g_names = []
    movieid = movie.get('genre_ids')
    for id in movieid :
        for a in genres_list:
            if a['id'] == id :
                g_names.append(a.get('name'))
    result = {
        'genre_names' : g_names,
        'id': movie.get('id'),
        'overview':movie.get('overview'),
        'title':movie.get('title'),
        'vote_average':movie.get('vote_average')
    }


    test = []
    test_dic = {'id' : 1,'power' : 2}
    test+=test_dic
    return result, test
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))