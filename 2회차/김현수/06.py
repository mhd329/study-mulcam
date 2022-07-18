import json
from pprint import pprint


def movie_info(movies, genres):
    movie_list = []
    for mov in movies:
        a = [] # a를 반복문에 넣어서 매번초기화 시켜줌.
    #print(type(movies.get('genre_ids'))) 리스트로 받았음
        for id in mov.get('genre_ids'):
            for dict in genres:
                if dict['id'] == id: #id값에 따른 영화이름 가져오기
                    #print(dict['name'],type(dict['name']))  #dict['name']은 string
                    a.append(dict['name'])
        resule = {
        'genre_names' : a,
        'id' : mov.get('id'),
        'title' : mov.get('title'),
        'overview' : mov.get('overview'),
        'vote_average' : mov.get('vote_average')
    }
        movie_list.append(resule)
    
    return movie_list
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))