import json
from pprint import pprint


def movie_info(movies, genres):
    movie2 = {}
    # t = list(len(movies['genre_ids']))
    for z in range(len(movies)) :
        genre_nameList = []
        t = list(movies[z]['genre_ids'])
        for i in range(len(movies[z]['genre_ids'])):
            for j in genres :
                # print(movies[z]['genre_ids'])

                if t[i] == j['id'] :
                    genre_nameList.append(j['name'])
                    movie2['genre_names'] = genre_nameList
                    movie2['id'] = movies[z]['id']
                    movie2['overview'] = movies[z]['overview']
                    movie2['title'] = movies[z]['title']
                    movie2['vote_average'] = movies[z]['vote_average']
        pprint(movie2)

    pass
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))