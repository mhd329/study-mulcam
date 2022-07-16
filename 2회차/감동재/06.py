import json
from pprint import pprint

def FindGenre(a):
   for g in genres_list :
        if g['id'] == a :
            return g['name']

def movie_info(movies, genres):

    Dics = []

    for movie in movies :
        Dic = {}
        Dic['genre_names'] =[]
        cnt = 0
        for i in movie['genre_ids'] :
            if cnt != 0:
                Dic['genre_names'].append(FindGenre(i))
            else:
                Dic['genre_names']=[FindGenre(i)]
            cnt+=1

        Dic['id'] = movie['id']
        Dic['title'] = movie['title']
        Dic['vote_average'] = movie['vote_average']
        Dic['overview'] = movie['overview']
        Dics.append(Dic)

    return Dics   
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    
    pprint(movie_info(movies_list, genres_list))