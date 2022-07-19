# 프로젝트 01 - 파이썬 기반 데이터 활용

## 주요 코드 및 해설

> 00~03 번 문제는 워낙 기본적인 예제라 스킵 함



### 04 번 예제

```python
movie_info = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    }
return movie_info
```

> 4, 5, 6 번 문제 중 가장 기본적인 뼈대가 되는 문제.
>
> 항목이 많을 경우 for문을 통해 빠르게 처리가 가능할 듯 하다. 하지만 이 경우엔 그냥 직접 나열하는 편이 가독성이 좋아 보여서 이렇게 작성했다.



### 05 번 예제

```python
genre_ids = movie['genre_ids']
    genre_names = []

    for genre in genres:
        if genre['id'] in genre_ids:
            genre_names.append(genre['name'])

    movie_info = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : genre_names
    }
    return movie_info
```

> 가장 어려웠던 문제.
>
> `genres.json` 파일은 dictionary로 이루어진 list이기 때문에 get을 쓸 경우 에러가 나서 한참 헤맸다. title등 다른 항목과는 다르게 `genre_ids`는 복수의 value가 들어갈 수 있기 때문에 다른 방식의 접근이 필요했다.
>
> 한참 고민해 본 결과 별도의 list `genre_names`를 만들어 `movie.json`의 `genre_ids` 의 value (18, 80)를 `genres.json` 의 key값으로 사용해 조회하고, 그 value값을 `genre_names` 에 저장했다. 그리고 직접 dictionary에 `genre_names`를 저장.



### 06 번 예제

```python
movie_info_list = []

    for m in movies:
        genre_ids = m['genre_ids']
        genre_names = []

        for genre in genres:
            if genre['id'] in genre_ids:
                genre_names.append(genre['name'])
        
        movie_info = {
        'id' : m.get('id'),
        'title' : m.get('title'),
        'vote_average' : m.get('vote_average'),
        'overview' : m.get('overview'),
        'genre_names' : genre_names
        }

        movie_info_list.append(movie_info)
    
    return movie_info_list
```

> 난이도 상으론 제일 어려운 문제지만 5 번 예제를 해결했다면 어찌 보면 가장 쉬운 문제였던 것 같다.
>
> 결과 예시를 보니 list형태인 것이 보였다. 그렇다면 5 번 예제의 코드를 그대로 for문을 돌려서 빈 list에 `movie_info` 를 하나 씩 넣으면 되는 것.
>
> 굳이 난점을 꼽자면 변수명이 비슷비슷해서 쓰다가 헷갈렸다. 



## 후기

json과 Dictionary. 둘 다 처음 다뤄보는 내용인 만큼 굉장히 어려웠다. 특히 `genres.json` 에 있는 list 안의 dictionary는 어떻게 접근해야 할지 한참 고민했다. 

뼈에 살이 조금씩 붙는 느낌. 이대로 배우면 조만간 그럴싸한 어플리케이션이 나올 것 같다. 

매우 만족!