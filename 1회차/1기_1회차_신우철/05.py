import json
from pprint import pprint


def movie_info(movie, genres):
    movie_data = {}
    name= {}
    for i in genres :
        name[i['id']] = i['name']

    names = []
    for j in movie['genre_ids'] :
        names.append(name[j])

    
    movie_data['genre_name'] = names
    movie_data['id'] = movie['id']
    movie_data['overview'] = movie['overview']
    movie_data['title'] = movie['title']
    movie_data['vote_average'] = movie['vote_average']
    return movie_data
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))