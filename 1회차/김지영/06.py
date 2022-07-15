import json
from pprint import pprint
from unittest import result


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.
    movie_list = []
    # movies.json이라는 파일을 보니까 딕셔너리를 요소로 갖는 리스트네요.
    # 리스트에서 바로 안의 요소에 접근을 못하니까 한번 movies라는 애를 한번 까봐야겠어요 
    # 그럼 리스트라는 애를 읽으면 딕셔너리에 접근할 수 있겠죠.
    for mov in movies:
        # print(mov)
        # 이제 이 딕셔너리에 접근할 수 있게 되었습니다. mov.get(key)로 value값에 접근합시다.
        def genres_name():
            genres_name = []
            # 'genre_ids'라는 key는 list를 value로 갖네요.
            # list는 key값으로 받아올 수 없으니까 한번 접근해서 list를 까줍시다.
            for gen_id in mov['genre_ids']:
                # print(gen_id)
                # 드디어 movies에 있는 장르id가 나왔어요!
                # 이제 이걸 genres의 id에 대조해봐야하는데
                # genres.json을 보니까 얘도 딕셔너리로 이루어진 list네요
                # list에서 바로 접근할 수 없으니까
                # genres도 까줍시다.
                for gen_num in genres:
                    # gen_num이라는 애가 나왔네요
                    # print(gen_num.get("id"))
                    # 얘는 딕셔너리니까 gen_num.get(key)로 value값에 접근해 줍시다.
                    if gen_id == gen_num.get("id"):
                        # 이제 대조한 애들을 어디다가 모아둡니다.
                        # 빈 리스트에다 append해줬어요
                        # 여기서 주의. 빈 리스트를 정의하는걸 for문 바깥에 두면 리스트 요소들이 계속 유지되니까 이전의 값을 유지하면서 계속 append해요.
                        # 모아두는 리스트는 for문이 돌때마다 다시 빈 리스트로 정의해줘야하니까 for문 안에 둡시다.
                        genres_name.append(gen_num.get("name"))
            # 장르이름을 모아둔 리스트를 리턴합니다.
            return genres_name
        result = {
            'genre_names' : genres_name(),
            'id' : mov.get('id'),
            'title' : mov.get('title'),
            'overview' : mov.get('overview'),
            'vote_average' : mov.get('vote_average')
        }
        # movie는 리스트니까 요소 하나하나를 읽고 result를 뱉을겁니다.
        # 이 result를 어디다 모아둬야 제가 볼 수 있겠죠
        # 빈 리스트에 append해줍시다.
        movie_list.append(result)
    # 리스트 movies의 요소를 읽은 result를 모아둔 리스트를 반환합니다.
    return movie_list
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))