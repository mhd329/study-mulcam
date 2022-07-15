import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
 
    f1 = open('data/movies.json','r',encoding ='utf-8')
    f2 = open('data/genres.json','r',encoding = 'utf-8')

    movies = json.load(f1)
    genres = json.load(f2)
        
    def findGenresName(list = []) : #장르 이름을 찾아주는 함수
        temp = []
        for i in genres:
            if i.get('id') in list:
                temp.append(i.get('name'))
        return temp
    
    for i in movies:
        results = {
            'genere_names' : findGenresName(i.get('genre_ids')),
            'id' : i.get('id'),
            'overview' : i.get('overview'),
            'title' : i.get('title'),
            'vote_average' : i.get('vote_average')
                
        }
        pprint(results)
    
        
       

        
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))