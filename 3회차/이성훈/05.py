import json
from pprint import pprint


def movie_info(movie, genres):
    movie2 = {}
    t = list(movie['genre_ids'])

    genre_nameList = []
    for i in range(len(t)):
        for j in genres :
            if t[i] == j['id'] :
                genre_nameList.append(j['name'])
                movie2['genre_names'] = genre_nameList
                # print(movie2['genre_names'])

    movie2['id'] = movie['id']
    movie2['overview'] = movie['overview']
    movie2['title'] = movie['title']
    movie2['vote_average'] = movie['vote_average']
    return movie2

    
    # 여기에 코드를 작성합니다.  

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))