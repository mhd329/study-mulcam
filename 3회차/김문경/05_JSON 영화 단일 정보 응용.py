import json
from pprint import pprint
# genres.json의 파일구조는 여러개의 딕셔너리들이 모인 리스트이고
# 그 안에는 id와 name이 있음(id, name은 키)
# genres를 반복문을 돌리면 개별 딕셔너리에 접근이 가능함
# 그 딕셔너리 안에서 는 id와 name이라는 key에 접근이 가능한데
# 각 딕셔너리에서 get한 id의 숫자값이 단일 영화(쇼생크 탈출)의 id 숫자값과 같다면
# 미리 만들어둔 빈 리스트에 append 하는것!
# 이제 딕셔너리를 return할 때 genre_names라는 key에 해당하는 value에 리스트를 넣으면 됨!!

def movie_info(movie, genres):
    mv_list = []
    for i in genres:
        for j in movie.get('genre_ids'):
            if j == i.get('id') :
                mv_list.append(i.get('name'))

    result = {
        'genre_names': mv_list,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
    }
    return result
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
