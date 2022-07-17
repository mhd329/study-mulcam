import json
from pprint import pprint


def movie_info(movies, genres):
    
    info = []
    
    for dict in movies:                                         # movies <type list>를 <type dict> 으로 반환
        first = {
            'id': dict.get('id'),
            'title': dict.get('title'),
            'vote_average': dict.get('vote_average'),
            'overview': dict.get('overview')
        }
    # first는 각 dict 안에 'id', 'title', 'vote_average', 'overview'가 있음

        genre_names = []
        for ids in dict['genre_ids']:
            for id in genres:
                if id['id'] == ids:
                    genre_names.append(id['name'])

        first['genre_names'] = genre_names                      # genre_names를 딕셔너리에 추가

        info.append(first)

    return info


    # 아래의 문제, genre_names에 장르 이름 하나밖에 안 나온다

    # info = []
    # genre_names = []

    # for all in movies:                          # movies <type list>에서 <type dict>으로
    #     for id_list in all.get('genre_ids'):    # all에 있는 딕셔너리 중 'genre_ids'를 반환하여 id_list로 만들기
    #         for genre in genres:                # genres <type list>에서 <type dict>으로
    #             if genre['id'] == id_list:
    #                 genre_names = []
    #                 genre_names.append(genre['name'])
                    
    #                 print(genre_names)

    # #     final = {
    # #         'genre_names': genre_names, 
    # #         'id': all.get('id'),
    # #         'title': all.get('title'),
    # #         'vote_average': all.get('vote_average'),
    # #         'overview': all.get('overview'),    
    # #     }
    # #     info.append(final)

    # # return info
    


        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))