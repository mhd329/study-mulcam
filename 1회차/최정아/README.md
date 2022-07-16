# 프로젝트 01 - 파이썬 기반 데이터 활용

## 배운 내용

```python
# oo
with open('00.txt', 'w', encoding='utf-8') as f:
    f.write("1회차 최정아\n")
    f.write("Hello, Python!\n")
    for i in range(1, 6):
        f.write(f'{i}일차 파이썬 공부 중\n')
```

:ok: 반복문을 활용하고 수업에서 배웠던 내용을 사용했습니다.

```python
# 01
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split()
    print(len(names))
```

:ok: Text의 길이를 카운트하고 출력을 했습니다.

```python
# 02
berry = set()
with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    text = f.read()
    # print(fruit, type(fruit))
    fruit = text.split('\n')
    # print(fruit, type(fruit))
    for name in fruit :
        if name.endswith('berry') == True :
            berry.add(name)

# print(len(berry))
# print(berry)
with open('02.txt', 'w', encoding='utf-8') as f :
    f.write(f'{len(berry)}\n')
    for i in range(len(berry)) :
        f.write(f'{berry.pop()}\n')
```

:ok:중복제거는 list(set())으로 했습니다.

```python
# 03
fruit = {}
with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    for line in f :
        newline = line.strip('\n')
        if fruit.get(newline, -1) == -1 :
            fruit[newline] = 1
        else :
            fruit[newline] += 1
with open('03.txt', 'w', encoding='utf-8') as f :
    for k, v in fruit.items() :
        f.write(f'{k} {v}\n')
```

:ok:딕셔너리를 활용해 키와 값으로 출력했습니다.

```python
# 04
import json
from pprint import pprint


def movie_info(movie):
    result = {}
    result['genre_ids'] = movie['genre_ids']
    result['id'] = movie['id']
    result['overview'] = movie['overview']
    result['title'] = movie['title']
    result['vote_average'] = movie['vote_average']

    return result 
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
```

:ok:딕셔너리와 get을 활용했습니다.

```python
# 05
import json
from pprint import pprint


def movie_info(movie, genres):
    result = {}
    genre_id_name = {}

    for d in genres :
        genre_id_name[d['id']] = d['name']

    genre_name = []
    for id in movie['genre_ids'] :
        genre_name.append(genre_id_name[id])
    movie['genre_names'] = genre_name

    result['genre_names'] = movie['genre_names']
    result['id'] = movie['id']
    result['overview'] = movie['overview']
    result['title'] = movie['title']
    result['vote_average'] = movie['vote_average']

    return result
    # 여기에 코드를 작성합니다.    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

:ok:for문과 list를 활용했습니다.

```python
# 06
import json
from pprint import pprint


def movie_info(movies, genres):
    result = []
    genre_id_name = {}

    for d in genres :
        genre_id_name[d['id']] = d['name']

    for i in range(len(movies)) :
        genre_name = []
        for j in movies[i]['genre_ids'] :
            genre_name.append(genre_id_name[j])
        movies[i]['genre_names'] = genre_name

    for d in movies :
        temp = {}
        temp['genre_names'] = d['genre_names']
        temp['id'] = d['id']
        temp['overview'] = d['overview']
        temp['title'] = d['title']
        temp['vote_average'] = d['vote_average']
        result.append(temp)
    return result
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

:ok:for문을 활용했습니다.



## 후기

조건문, 반복문, 파일 입출력을 통한 데이터, 텍스트 및 JSON 데이터의 활용을 목표로 문제를 풀었는데 수업에서 배웠던 내용을 문제 접근 방식에 활용할 수 있었습니다. 배운지 얼마 되지 않았지만 그동안 컴퓨팅 사고가 많이 개선되었고 계속 문제를 푸는 반복 학습을 통해 발전해야 겠다고 생각했습니다. 