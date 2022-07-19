import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    genre_ids = movie.get('genre_ids')
    # print(genre_ids)
    res = []
    # print(genres[0])    # {'id': 28, 'name': 'Action'}
    # g = genres[0]   # 28
    # print(g.get('name'))

    # print('len', len(genres))

    for id in genre_ids:
        # print('id', id)
        for j in range(len(genres)):
            # print('id', id)
            # print('genres[j]', genres[j])
            if (id == genres[j].get('id')):
                # print('append', genres[j].get('name'))
                res.append(genres[j].get('name'))
                break
    return {
        'genre_names': res,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))