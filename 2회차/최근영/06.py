import json
from pprint import pprint


def movie_info(movie, genres_list):
    answer=[]
    for i in range(0, len(movie)):
        new_genres_list=find_geners(movie[i].get('genre_ids'),genres_list)
        answer.append({
        'genre_names' : new_genres_list,
        'id' : movie[i].get('id'),
        'overview' : movie[i].get('overview'),
        'title' : movie[i].get('title'),
        'vote_average' : movie[i].get('vote_average')
        })
    return answer

def find_geners(movie,genres_li):
    re_list=[]
    for i in range(0, len(movie)):
        for j in genres_li:
            if j['id'] == movie[i]:
                re_list.append(j['name'])
    return re_list


        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)
    
    pprint(movie_info(movies_list, genres_list))