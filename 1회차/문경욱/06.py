import json
from pprint import pprint


def movie_info(movies, genres):
    # movie.json과 movies.json의 차이는 movie는 하나, movies는 여러개
    # movies_list[0] = adult, backdrop_path, ... , vote_count까지 다 나옴.
    # movies_list[0]에 있는 항목들은 어떻게 꺼낼 것인가? -> movies_list[0]['키값]
    # info_dict에 1차로 dict을 만든 후 result_list에 dict 전부를 추가.


    result_list = []

    for i in range(20):
        movie_ids = movies_list[i]['genre_ids']
        movie_id = movies_list[i]['id']
        movie_overview = movies_list[i]['overview']
        movie_title = movies_list[i]['title']
        movie_average = movies_list[i]['vote_average']

        movie_gen_names = [] # 장르 이름을 추가할 list
        for genre_id in movie_ids: # movie.json 에 있는 쇼생크탈출의 genre
            for genre in genres: # genres.json 에 있는 genre 리스트
                if genre_id == genre["id"]: # 만약 genre 리스트에 있는 키값과 movie_ids에 있는 genre_id의 값이 같으면
                    genre_name = genre["name"] # genre_name에 movie_ids에 있는 키값에 대응되는 value를 집어넣고
                    movie_gen_names.append(genre_name) # 장르 이름을 추가할 list에 genre_name을 집어넣는다.

        info_dict = {} # 전체 information_dict
        info_dict['genre_ids'] = movie_gen_names
        info_dict['id'] = movie_id
        info_dict['overview'] = movie_overview
        info_dict['title'] = movie_title
        info_dict['vote_average'] = movie_average
        result_list.append(info_dict)


    return result_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))