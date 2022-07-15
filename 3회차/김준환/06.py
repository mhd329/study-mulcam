import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  

    f_movies = open('data/movies.json', 'r', encoding='utf-8')    
    f_genres = open('data/genres.json', 'r', encoding = 'utf-8')
    mvs = json.load(f_movies)
    gr = json.load(f_genres)
    lst = []
    mv_pop_score = []
    popular_idx = []
    hot_mv = []
    mvs_idx = []
    for i in range(len(mvs)):
        mv_pop_score.append(mvs[i]['popularity'])

    popular_idx = mv_pop_score
    popular_idx.sort(reverse=True)
    count = 0
    for score in popular_idx:
        count += 1
        mvs_idx.append(mv_pop_score.index(score))
        if count == 20:
            break
    for hot_idx in mvs_idx:
        mv = mvs[hot_idx]
        lst = []
        for i in mv.get('genre_ids'):
            for n in range(len(gr)):
                if gr[n]['id'] == i:
                    lst.append(gr[n]['name'])

        result = {
            'genre_names' : lst,
            'id' : mv.get('id'),
            'title' : mv.get('title'),
            'vote_average' : mv.get('vote_average'),
            'overview' : mv.get('overview'),
        }

        pprint(result)    
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))