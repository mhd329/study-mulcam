import json
from pprint import pprint


def movie_info(movie, genres):
    movie_ids = movie['genre_ids']
    movie_id = movie['id']
    movie_overview = movie['overview']
    movie_title = movie['title']
    movie_average = movie['vote_average']

    movie_gen_names = [] # 장르 이름을 추가할 list
    for genre_id in movie_ids: # movie.json 에 있는 쇼생크탈출의 genre
        for genre in genres: # genres.json 에 있는 genre 리스트
            if genre_id == genre["id"]: # 만약 genre 리스트에 있는 키값과 movie_ids에 있는 genre_id의 값이 같으면
                genre_name = genre["name"] # genre_name에 movie_ids에 있는 키값에 대응되는 value를 집어넣고
                movie_gen_names.append(genre_name) # 장르 이름을 추가할 list에 genre_name을 집어넣는다.


    info_dict = {} # 출력 information_dict
    info_dict['genre_ids'] = movie_gen_names
    info_dict['id'] = movie_id
    info_dict['overview'] = movie_overview
    info_dict['title'] = movie_title
    info_dict['vote_average'] = movie_average

    return info_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))