# 프로젝트 01 - 파이썬 기반 데이터 활용

## 문제 해설

## 1번 문제

```python
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')
    cnt = 0
    for i in fruits: 
        cnt += 1
    print(cnt)
with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt))
```

텍스트를 **공백** 기준이 아닌 **개행** 기준으로 나눠야만 띄어쓰기된 과일 이름이 온전히 하나로 인식되어 총 과일 개수가 나왔다.

`fruits = text.split('\n')`

- 계속 헤메다가 조금 뒤쳐진다는 느낌 때문에 조급해져서 디스코드로 결정적인 힌트를 받아버렸다..
- 단순히 count만 출력해서 전전긍긍 할게 아니라 직접 fruits를 같이 출력해서 이름을 확인했어야 했다.

## 2번 문제

```python
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = set(text.split('\n'))
    cnt = 0
    be = []
    for i in fruits:
        if i.endswith('berry'):
            cnt += 1
            be.append(i)
    result = '\n'.join(map(str,be))
    # print(cnt)
    # print(result)
    

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{str(cnt)}\n')
    f.write(result)
```

과일 중 berry들만 남기는 건데

1. `set()`으로 중복을 없애고 
2. `if i.endswith('berry')`로 berry들만 남겨놓고 리스트에 담아서 문자열로 출력했다

- 혼자의 힘으로만 풀어서 뿌듯했다!
- 파일 입출력의 f.write()에서 string인자 하나만 받는다는 것을 모르고 좀 해멨다...

## 5번 문제

```python
ids= movie['genre_ids']
    l = []
    for i in ids:
        for j in genres:
            if i == j['id']:
                l.append(j['name'])
    names = { 'genre_names' : l }
    movie.update(names)
    m = {
        'genre_names': movie.get('genre_names'),
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }
    return(m)
```

1. `movie의 id 키값`을 `for문`에 넣고 

2. 그 안에 `genres`를 `for문`에 넣어서

3. `if문`으로 `movie의 id값`과` genres의 id값`을 같은지 비교했다.

4. 참이면 리스트에 `genres의 name값`을 추가했다.

   `l.append(j['name'])`

5. 그 리스트를 names라는 딕셔너리에 밸류로 넣고

   `names = { 'genre_names' : l }` 

6. `movie.update(names)`로 movie 딕셔너리에 업데이트해서 추가했다.

- genres의 name값이 들어간 리스트를 어떻게 movie에 적용할까 고민하다가 리스트를 딕셔너리로 바꿔서 업데이트 하는 식으로 했다. 좋은 방법인지는 모르겠다..
- 덕분에 딕셔너리와 리스트에 대한 공부가 많이 된 것 같다.
- 적절한 메소드들이 아직 기억이 잘 안나서 외워야 할 것 같다..

## 6번 문제

```python
    my_movie = []
    for movie in movies:
        ids= movie['genre_ids']
        l = []
        for i in ids:
            for j in genres:
                if i == j['id']:
                    l.append(j['name'])
        names = { 'genre_names' : l }
        movie.update(names)
        m = {
            'genre_names': movie.get('genre_names'),
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average')
        }
        my_movie.append(m)
    return(my_movie)
```

1. 5번 코드에서 맨위에 `for movie in movies` 추가하고

2. 새로운 리스트에다 전체적인 반복문을 `.append`로 추가했다.

- `for movie in movies`로 여러 영화들을 반복해서 넣어주는 점이 포인트 같다.
- 마지막 두 줄 `my_movie.append(m)`,`return(my_movie)`의 들여쓰기 위치가 좀 헷갈렸다..

## 후기

### 아쉬웠던 점

1. 100% 나의 힘으로만 문제를 다 푼게 아니라는 점이 제일 아쉽다😥

2. 딕셔너리, 리스트, 메소드 활용이 능숙하지 못한 것 같다.

   

### 좋았던 점

1. 그래도 최대한 혼자서 풀었다!

2. 막힐 때마다 `print(type()`) 해보는 습관이 들여졌다.

3. 딕셔너리 활용하는 방법을 많이 배워서 좋았다.

4. 조건문, 반복문이 좀 더 능숙해진 느낌이다!

5. 약 10시간을 몰입해서 코딩한게 뿌듯하다! 

   적성에 잘 맞아서 다행이다🥳