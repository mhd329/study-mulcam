import json
from pprint import pprint


def movie_info(movies, genres):
    movies_li = []  # new_dict 를 담을 movies_li 빈 리스트 생성
    for movie in movies:  #movies 라는 리스트 안의 movie 라는 딕셔너리 반복
        li = ['id', 'title', 'vote_average', 'overview', 'genre_ids']  # 일치하는 key 값 리스트
        new_dict = {} # 키 값이 일치했을 때, 추가할 빈 딕셔너리 생성
        for key, value in movie.items(): # 딕셔너리 안의 key 값이 li 리스트에 있을 때, new_dict 딕셔너리에 추가
            if key in li:
                new_dict[key] = value
        movies_li.append(new_dict) # new_dict 딕셔너리를 movies_li에 추가
    
    for movie in movies_li: # movies_li 라는 리스트에 movie 라는 딕셔너리를 반복
        for genre in genres: # genres 리는 리스트에 genre 라는 딕셔너리를 반복
            for idx in range(len(movie['genre_ids'])): # movie 라는 딕셔너리의 키값이 genre_ids 인 value 값은 리스트 type임으로 idx라는 인덱스로 반복

                if movie['genre_ids'][idx] == genre['id']: # idx 인덱스 값이 genre 딕셔너리 안의 key 값이 id인 value 값과 같을 때, idx 인덱스 값을 genre 딕셔너리 안의 key 값이 name인 value 값으로 변경
                    movie['genre_ids'][idx] = genre['name']
        movie['genre_names'] = movie.pop('genre_ids')
    return movies_li

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))