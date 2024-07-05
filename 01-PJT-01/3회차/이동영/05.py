import json
from pprint import pprint
from unicodedata import name


def movie_info(movie, genres):
    pass 
    f1 = open('data/movie.json','r',encoding ='utf-8')
    f2 = open('data/genres.json','r',encoding = 'utf-8')

    movie = json.load(f1)
    genres = json.load(f2)
    

    def findGenresName() : #장르 이름을 찾아주는 함수
        temp =[]
        for i in genres:
            if i.get('id') in movie.get('genre_ids') :
                    temp.append(i.get('name'))
        return temp
   
    results = {
        'genere_names' : findGenresName(),
        'id' : movie.get('id'),
        'overview' : movie.get('overview'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    pprint(results)
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))