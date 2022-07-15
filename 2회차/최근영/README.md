# 프로젝트 01 - 파이썬 기반 데이터 활용
  00. 간단한 문서를 불러오는 기본적인 내용을 물어보는 것

```python
    with open("00.txt",'w',encoding='utf-8') as f:
        f.write("2회차 최근영\n")
        f.write("Hello, Python\n")
        for i in range(1, 6):
            f.write(f'{i}일차 파이썬 공부 중\n')
```

   - with를 이용하여 문서를 생성할 줄 아는것인지?
   - 반복문을 제대로 이해했는지? 등을 물어보는 코드

  01. 다른 폴더의 데이터를 가져와 활용 할 수 있는지 물어보는 내용

```python
    with open(r"data/fruits.txt",'r',encoding='utf-8') as f:
        datas = f.read()

    cnt=0
    data_list = datas.split('\n')
    for i in data_list:
        cnt+=1

    with open('01.txt', 'w', encoding='utf-8') as f:
        f.write(str(cnt))
```

   - open으로 가져올 데이터의 경로를 가져오는데 r을 붙인 이유는 \f \n 등 인식하는 것을 방지하기 위해 찾아서 넣어줌.
   - datas에 불러온 자료를 저장한 후 데이터를 가공한 다음 가공이 끝난 데이터를 문서를 작성해서 넣어주는 방식을 사용함.


   02. 1번문제에서 확장된 문제로 가져온 데이터를 수정할 수 있는지

```python
    with open(r"data/fruits.txt",'r',encoding='utf-8') as f:
    datas = f.read()

    cnt=0
    data_list = datas.split('\n')
    new_list = []
    for i in data_list:
        print(i)
        if i[-5:] == 'berry':
            new_list.append(i)

    answer = set(new_list)

    with open(r"02.txt", 'w', encoding='utf-8') as f:
        f.write(str(len(answer)))
        for i in answer:
            f.write(f"\n{i}")
```

   - 1번문제와 비슷한 구성이지만 내가 원하는 문자가 있는지 찾아보는 방식
   - 'berry' 라는 문자가 있는지 찾는 문제 (문자가 여러개면 안되니 중복 제거)
   - berry라는 이름이 붙은 문자를 다 찾는것을 목표로 함.
   - beery라는 말이 끝에 와야한다 했으므로 슬라이싱을 이용하여 끝에서 5글자가 berry 인것들만 찾음.
   - 이후 중복제거한 후 결과물을 메모장에 기록

   03. 데이터를 가지고 몇번 사용됐는지 확인하는 방법

```python
    with open(r"data/fruits.txt",'r',encoding='utf-8') as f:
        datas= f.read()


    datas = datas.split('\n')
    fruits_dict = {}
    for i in datas:
        if i in fruits_dict:
            fruits_dict[i] += 1
        else:
            fruits_dict[i] = 1

    with open('03.txt', 'w', encoding='utf-8') as f:
        for key,value in fruits_dict.items():
            f.write(f'{key} {value}\n')

```

   - 데이터 가져오는 방식은 앞과 동일하지만 dict를 사용하여 데이터의 값과 빈도를 넣어줄려고 dictionary를 사용
   - 빈 dictionary 선언 후 list의 이름이 dictionary에 존재하면 value 값을 증가 없으면 dictionary 추가

   04. 함수를 이용하여 내가 원하는 값 출력
```python
    import json
    from pprint import pprint


    def movie_info(movie):
        answer = {
            'genre_ids' : movie.get('genre_ids'),
            'id' : movie.get('id'),
            'overview' : movie.get('overview'),
            'title' : movie.get('title'),
            'vote_average' : movie.get('vote_average')
        }
        return answer
            


    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        movie_json = open('data/movie.json', encoding='UTF8')
        movie = json.load(movie_json)
        
        pprint(movie_info(movie))
```

   - dictionary 를 사용하여 함수의 구조를 만들어 return 값을 통하여 내가 원하는 값들만 출력할 수 있도록 반환

   05. 영화 장르 추가
```python
    import json
    from pprint import pprint


    def movie_info(movie, genres_list):
        
        new_genres_list=find_geners(movie.get('genre_ids'),genres_list)
        answer = {
            'genre_names' : new_genres_list,
            'id' : movie.get('id'),
            'overview' : movie.get('overview'),
            'title' : movie.get('title'),
            'vote_average' : movie.get('vote_average')
        }
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
        movie_json = open('data/movie.json', encoding='UTF8')
        movie = json.load(movie_json)

        genres_json = open('data/genres.json', encoding='UTF8')
        genres_list = json.load(genres_json)

        pprint(movie_info(movie, genres_list))
```

   - 방법이 따로 생각나지 않아서 함수를 만들어서 영화의 장르번호를 넣으면 그 장르번호를 무슨 장르인지 값으로 반환해주는 함수를 생성

   - 그 함수를 기존의 영화정보 반환하는 함수내부에 넣어서 코드를 구성후 최종적으론 answer이라는 정보를 반환

   06. 영화 한개가 아닌 여러개를 출력

```python
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
```
   - 5번에서 사용한 코드에서 영화 한개가 아닌 여러개의 리스트를 다루도록 리스트를 추가해줌
   - 그 외에는 별로 바뀐점이 없음.
   

## 후기
  - 딕셔너리와 리스트를 병행으로 섞어서 사용하니 오류가 자주 발생했던 것 같다.
  - 실제 데이터를 다룰때는 리스트 내부에 딕셔너리 형태의 자료가 많은것 같은데 좀 더 다뤄보고 싶다.
  - 오늘 실습을 통해 내 수준이 어느정도인지 파악할 수 있어서 좋았던 것같다.
  - 뭔가 내용을 물어보고싶은데 다른 분들께 실례가 될 것 같아서 물어보기 조금 조심스럽다?
  - 재밌다 ㅎㅎㅎ
  - 강의를 들으면서 내가 몰랐던 부분과 잘못 이해했던 부분을 제대로 짚고 넘어가는 것 같다.
  - 주말에 복습을 무조건 해야겠다는 생각이 든 프로젝트 였다.

 