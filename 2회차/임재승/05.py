import json
from pprint import pprint


def movie_info(movie, genres):
    new = {}
    gen_list = []

    # print(movie.get('genre_ids'))
    for num in movie.get('genre_ids'):
        # print('삐비비비비비비비빅')
        # print(num)
        for gen in genres:
            if num == gen['id']:
                gen_list.append(gen['name'])
    new['genre_names'] = gen_list
    new['id'] = movie['id']
    new['title'] = movie['title']
    new['vote_average'] = movie['vote_average']
    new['overview'] = movie['overview']

    return new
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))


