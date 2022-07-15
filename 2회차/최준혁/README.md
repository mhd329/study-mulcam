# 프로젝트 01 - 파이썬 기반 데이터 활용



## 문제 풀이

<br>

 ``` python
 # 0번
 with open('00.txt', 'w', encoding='utf-8') as f:
     f.write("2회차 최준혁\n")
     f.write("Hello, Python!\n")
     for i in range(1, 6):
         f.write(f'{i}일차 파이썬 공부 중\n')
 ```

📌 딱히 설명할게 없는 문제이기도 하다. 오늘 배운것들을 그대로 썼는데 출력이 한 줄로 나오기때문에 `\n` 으로 개행하고 반복문을 통해서 숫자만 반복되는 문장을 출력했다.

<br>

``` python
# 1번
import sys

with open(r"/Users/mac/Desktop/KDT_PROJ/01-PJT-01/2회차/최준혁/data/fruits.txt", 'r', encoding='utf-8') as f:
    text = f.readlines()
    cnt = 0

    for i in range(len(text)):
        cnt += 1    
    print(cnt)

sys.stdout = open('01.txt', 'w')
print(cnt)
sys.stdout.close()
```

📌 이 문제를 시작하면서 첫번째 오류에 부딪혔다. `fruits.txt` 파일의 경로를 찾을 수 없었는데 위와 같이 `r"경로"` 를 입력해서 해결했다.

내용은 읽어들인 text의 길이만큼 카운트를 하고 출력을 한 후 저장을 하는 문장이다.

<br>

``` python
# 2번
import sys
with open(r"/Users/mac/Desktop/KDT_PROJ/01-PJT-01/2회차/최준혁/data/fruits.txt", 'r', encoding='utf-8') as f:
    text = f.readlines()
    lines = list(set(text))
    cnt = 0
    end_berry = []
    for name in lines:
        if 'berry' in name:
            cnt += 1
            if name.startswith('berry'):
                cnt -= 1
                continue
            end_berry.append(name)
            print(name)
    print(cnt)

sys.stdout = open('02.txt', 'w')
for i in range(0, 18):
    print(end_berry[i])
print(cnt)
sys.stdout.close()
 
```

📌 2번 문제는 읽어들인 과일들 중에 `list(set())` 으로 중복을 제거하고 `berry` 라는 이름을 가진 과일들을 가져와서 카운트하고, 문장 앞에 berry가 붙은 과일은 빼서 ` end_berry = []` 에 집어넣는 방식을 사용했다. 

<br>

``` python
# 3번
from select import kevent
import sys

with open(r"/Users/mac/Desktop/KDT_PROJ/01-PJT-01/2회차/최준혁/data/fruits.txt", 'r', encoding='utf-8') as f:
    text = f.read()
    fruit = text.split("\n")
    dict_fruit = {}

    for char in fruit:
        if char in dict_fruit:
            dict_fruit[char] += 1
        else:
            dict_fruit[char] = 1

    for v, k in dict_fruit.items():
        print(v, k, end='')

sys.stdout = open('03.txt', 'w')
for k, v in dict_fruit.items():
    print(k, v) 
sys.stdout.close()

```

📌 3번 문제는 전에 풀었던 dictionary와 비슷한 방식으로 풀었는데 딕셔너리에서는 같은 이름의 과일이 두 번 들어가도 키나 값에선 하나만 출력되는데, 들어있는 과일의 수를 카운트해서 키와 값으로 출력되게 했다.

<br>

``` python
# 4번
import json
from pprint import pprint


def movie_info(movie):
    # genre_ids
    # overview
    # title
    # vote_average    
    shawshank = movie # 이름을 쇼생크라고 짓고싶었어요
    result = {
        'genre_ids'     : shawshank.get('genre_ids'),
        'overview'      : shawshank.get('overview'),
        'title'         : shawshank.get('title'),
        'vote_average'  : shawshank.get('vote_average')
    }
    return result
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))

```

📌 4번 문제는 받았던 힌트 그대로 딕셔너리의 키를 적고 get으로 값을 받아오는게 다였다.

<br>

``` python

# 5번
import json
from pprint import pprint


def movie_info(movie, genres):
    # movie
    # genres_list
    g_names = [] # name값 담을 리스트
    shawshank = movie
    for ids in shawshank.get('genre_ids'): # movie의 장르 id 18, 80
        for id in genres: # genres에서 
            if ids == id.get('id'): # movie의 genre_ids와 같은게 있으면
                g_names.append(id.get('name')) # 리스트에 추가 

    result = {
        'genre_names'  : g_names,
        'genre_ids'    : movie.get('genre_ids'),
        'overview'     : movie.get('overview'),
        'title'        : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    return result
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

📌 5번 문제부터 시간이 오래걸렸던것 같다. `genre_name` 을 4번과 같이 가져오려니 get을 사용할 수 없어서 for문으로 가져왔다. `shawshank(movie)` 의 `genre_ids`를 `genres` 의 `id`와 비교하여 같은것들의 `name`을 리스트에 담는 방법을 사용했다. 

<br>

``` python
# 6번
import json
from pprint import pprint

def movie_info(movies, genres):

    m_result = []
    for all in movies:
        for ids in all.get('genre_ids'): 
            for id in genres:
                if ids == id.get('id'): 
                    g_names = []
                    g_names.append(id.get('name')) 

        result = {
            'genre_names'  : g_names,
            'genre_ids'    : all.get('genre_ids'),
            'overview'     : all.get('overview'),
            'title'        : all.get('title'),
            'vote_average' : all.get('vote_average')
        } 
        m_result.append(result) 
    return m_result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    #movie_info(movies_list, genres_list)
    pprint(movie_info(movies_list, genres_list))
```

📌 6번은 크게 다를건 없었다. for 문을 하나 더 덧씌우고 비교대상이 달랐을 뿐이다.

<br>



## 💬 후기

처음 하는 파이썬이라 아직도 모르는 개념이 많다. 그나마 오래 써본 언어라고는 델파이 정도밖에 없는데 델파이를 접하다가 파이썬을 접하니 참 유연성이 많아보인다. 문제를 풀면서도 아직까지 생각하는 능력이 모자라다는걸 느끼고 있다. 이번 기회에 내 부족한 점들을 많이 채워서 더 높은곳을 향할 수 있도록 많이 신경써야할것 같다. 마지막 후기를 적을 때 즈음엔 '발전했다', '성장했다' 는 말을 꼭 남기고싶다. 