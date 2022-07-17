# 프로젝트 01 - 파이썬 기반 데이터 활용

## 후기

### 1. 코드 및 해설

#### 00. 텍스트 데이터 출력

> .txt 파일을 생성하고 내용 입력하기, '\n'을 주의할 것

```python
with open('00.txt', 'w', encoding='utf-8') as f:
    f. write("     "+"3회차 안예지\n")
    f. write("Hello, Python!\n")
    for i in range(1, 6) :
        f. write(f'{i}일차 파이썬 공부 중\n')
```



#### 01. 텍스트 데이터 입력

> 파일 불러와서 다른 .txt 파일에 원하는 값 입력하기

```python
with open('fruits.txt', 'r', encoding='utf-8') as f :
    # fruits 열었음
    names = f.read().split('\n')
    # print(text)
    cnt = 0
    # print(names)
    for i in names:
        cnt += 1
with open('01.txt','w' , encoding='utf-8') as f :
    f. write(f'{cnt}')
       
 
    # 줄바꿈은 공백으로 쪼갤 수 있음
```



#### 02. 텍스트 데이터 활용 - 특정 단어 추출

> 파일을 열고 'berry'로 끝나는 글자에 접근해서 해당 글자 추출해오기

```python
with open('fruits.txt', 'r', encoding='utf-8') as f:
    # 일단 열어서 읽어와
    
    names = f.read().split('\n')
    # print(names, type(names))
    # print(type(names))

    cnt = 0
    berry = []
    new_list = []
    # 'berry'로 끝나는 글자들을 만났을 때만 담는 통
    # 중복문 제거한 리스트
    # 1. 문자를 슬라이싱 해보기
    for n in names :
        if n[-len('berry')::1] == 'berry':
            # 마지막 글자까지 진행해야 하므로 글자 수의 음의 인덱스부터 
            # 마지막 글자까지 1씩 증가하며 진행
            # cnt += 1
            # 마지막 글자가 berry 로 끝나는 요소만 찾기 정상 적용 확인
            berry += [n]
            for m in berry : 
                if m not in new_list :
                    # 중복되는 끝berry 과일 찾아서 첨 보는 애들만 통에 넣기
                    cnt += 1
                    new_list += [m]
                    
    with open('02.txt', 'w', encoding='utf-8') as f:
        f. write(f'{cnt}\n')
        f. writelines('\n'.join(new_list))
```



#### 03. 텍스트 데이터 활용 - 등장횟수

> 딕셔너리의 생성원리와 get 메소드의 이해가 필요

```python
with open('fruits.txt', 'r', encoding='utf-8') as f :
    text = f.read().split('\n')
    # print(text)
    # 똑바로 리스트업됐는지 확인
    fruit_dict = {}
    for word in text :
        # 리스트 text를 돌면서 
        fruit_dict[word] = fruit_dict.get(word, 0) + 1 
        # 과일 사전의 key word의 value는 
        # 과일 사전에 key가 있으면, 해당 key의 기존 value를 반환합니다.
        # 과일 사전에 key가 없으면, 해당 키 word의 값을 0으로 
        # 반환하여 초기화합니다.
        # 반환되는 값이 Nope일 경우 해당 
        # type은 nonetype이므로 뒤에 +1과 연산이 되지 않습니다.
        # fruit_dict[word] = fruit_dict.get(word) + 1 
        # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
        # word에 바인딩되는 키의 값은 무조건 1개 이상 존재하므로
        # 순회를 할때마다 해당 word의 value에 1을 추가합니다.
    upper = sorted(fruit_dict.items())
    fruit_dict = dict(upper)
with open('03.txt', 'w', encoding='utf-8') as f :
    for name in fruit_dict : 
        sorted(fruit_dict)
        f.write(f'{name} {fruit_dict[name]}\n')
        
```



#### 04. JSON 데이터 활용 - 영화 단일 정보

> 리스트와 딕셔너리 타입의 접근법이 다름을 이해하기(리스트는 인덱스, 딕셔너리는 [Key]이다.) 하지만 본인은 함수가 어려웠다. 단순히 결과를 출력하는 것이 아닌, 보여주고자 하는 것을 input으로 정의하는 방법과 보여줘야할 output이 무엇인지 고민을 많이 했다.

```python
def movie_info(movie):
    result = {
        'id' : movie.get('id'),
        # .get은 딕셔너리 타입에서 접근가능한 메소드이다.
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    }
    return result
```



#### 05. JSON 데이터 활용 - 영화 단일 정보 응용

> 리스트와 딕셔너리의 접근법이 다름을 항상 명심해야 한다.
>
> 그리고 함수 안에는 for문이 들어갈 수 있다. for문의 바인딩 진행 순서를 이해하기

```PYTHON
def movie_info(movie, genres):
    
# 리스트 genres의 인덱스를 순회
# n번째 딕셔너리의 키의 값이 리스트 genre_ids의 요소 값과 같다면
# genre_ids에 n번째 딕셔너리의 name키의 값을 추가
    genre = []
    # 장르 정보를 담을 통
    for x in movie['genre_ids'] :
        # movie 안의 'genre_ids' 키의 값인 리스트를 순회하는 x
        # x = 18일 때, 
        for y in range(len(genres)) :
            if genres[y]['id'] == x :
                genre += [genres[y]['name']]
                
    
    result = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : genre
    }
    
    return result
```



#### 06. JSON 데이터 활용 - 영화 다중 정보 활용

> for문의 진행 순서를 이해하고, 바인딩 되는 시점의 코드를 이해하기

```python
def movie_info(movies, genres):
    # cnt = len(movies) : 20
    # vote_average에 대해서 줄세우기 할 필요는 없다.(감사합니다)
    
    result = {}
    answer = []
    
    for x in range(len(movies)):
        genre = []
        # genre 값을 전체 movies를 순회할 때마다 초기화
        # = 매 영화마다 장르는 다르기 때문이다.
        for y in movies[x]['genre_ids'] :
            # movies 의 x번째 요소인 딕셔너리에서 키 'genre_ids'값을 반환
            for z in range(len(genres)) :
                # genres 안의 리스트를 순회하면서
                if y == genres[z]['id'] :
                    # 'genre_ids'의 값이 
                    # genres 리스트의 z번째 딕셔너리에서
                    # 키 'id'의 값이 같다면
                    genre += [genres[z]['name']]
                    # genre 리스트에 같은 딕셔너리의 키 'name'의 값을 추가한다.
                    result = {
             'id' : movies[x].get('id'),
             'title' : movies[x].get('title'),
             'vote_average' : movies[x].get('vote_average'),
             'overview' : movies[x].get('overview'),
             'genre_names' : genre
            }
                    answer += [result]
    
    return answer
```





### 2. 배운 점, 느낀 점

1. **파이썬튜터는 최고의 프로젝트 파트너였다.** 📉

덕분에 for문이 중첩 진행될 때 가장 아래에 있는 바인딩 값은 가장 먼저 모든 범위를 순회한다는 것을 알게 됐다. 해당 for문의 순회가 끝나야 다시 가장 바깥쪽 for문이 다음 바인딩값으로 넘어갈 수 있다.

2. **그래도 역시 피어러닝이 최고다.** 👥

함수 안에 for 문이 들어갈 수 있다는 것을 for 문 없이 output 값을 내려는 시도로 5시간을 사투한 끝에 다른 수강생 분들의 코드를 통해 알게 됐다. 그 날은 밤을 쫄딱 샜다.

3. **리스트는 인덱스, 딕셔너리는 키 값으로 접근하며🤦‍♀️**

 for n in range(5)의 순회 횟수는[0,1,2,3,4]로 5회, len(5)=5와 같다. 진짜 헷갈린다.

초기값은 너무 중요하다. 너무너무.



**그리고** 

 현재 시간은 새벽 3시다. 첫 프로젝트가 공개된 금요일부터 지금까지 3시 이전에 잠든 기억이 없다. 하지만, 그 끝에 나는 6문제를 나의 풀이로 설명하고, 출력해 내는 데 성공했고 그 과정에서 개념을 확실히하는 시간을 가질 수 있었다. 모두가 자는 시간임에도 서너 시간은 우습도록 모니터만 바라보고 손가락 외에는 미동도 없이 우뚝 앉아 있었지만, 전혀 지루하지 않았다. 그 점이 신기했다. 시간을 낚는 강태공도 아닌데 그렇게나 많은 시간을 무언가 단 하나에 집중할 수 있는 것이 신선했다. 그렇게 6시간 가량을 앉아있으면 문제가 풀렸다. 그렇게 금,토,일 사흘동안 하루 하나씩, 3문제를 풀어냈다. 

금요일 수업 막바지에 진행했던 zoom 해설 녹화 영상이 올라왔으면 더 빨리 풀렸을지도 모른다. 기억에 의존해서 강사님이 주신 힌트를 곱씹어봤지만, 6번 문제에 대한 힌트는 아직 이해 못했다. 복사 붙여넣기만 하면 된다고 했던 것 같은데, 나는 그런 간단한 과정이 아니었다. 

물론 그 과정에 좌절감은 없었다. 좌절하기엔, 지금은 너무 초반이었다. 한편으로는 그래서 두렵다. 초반부터 적성 유무에 대해 돌이켜보게 되는 코딩이라는 작업을, 내가 앞으로 얼마나 소화해낼 수 있을지. 걱정이 몰려오는 것도 사실이다. 그럼에도 결국 내가 원하는 값을 구현해 냈다는 것으로부터 오는 성취감, 성장했다는 자신감은 그에 견줄 바가 당연히 못 된다. 

 나의 코드는 상당히 어지럽다. 언젠간 간결해지겠지, 지금의 내가 생각할 단계는 아니라고 생각한다. 나는 언어를 배우고 있고, 이제야 기역 니은 디귿을 겨우 읊는다. 왜 나의 기역이 세워놓은 낫보다 비뚤은지, 다른 사람의 기역보다 꾸불한지 생각할 여력이 없다. 더 배우고, 더 익숙해져서 또박또박 '가'를 써내기 위해 앞만 봐야 하기 때문이다. 그런데 그 시점에서 오는 한 가지의 딜레마가 있었다.

바로 구글링이다. 구글링 속 코드들은 깔끔하다. 주 4회의 개념 수업 진행동안은 이 바로 다음 단계인 ''알고리즘 문제풀이'' 진행을 위해 논리로 먼저 접근하는 것이 기본 자세였고, 구글링은 그 분야엔 별 기여가 못 됐다. 보통은 메소드로 뚝딱 구현해버렸기 때문이었다. 나는 실제로 수업 진행 중 구글링을 통해 쉽게 푼 문제가 사실은 어려운 반복문 구조로 구현되는 것이 수업의 목표였다면 해당 문제를 check-up 해제 표시하기도 했다. 

하지만 처음 마주한 프로젝트 환경에서 나는 구글링을 자유롭게 활용해도 되는 상황에 놓였고, '이렇게 해도 되는 건가,'라는 낯선 환경을 경계하는 맘이 앞섰다. 그리고 프로젝트를 진행하면서 결국 나의 구심점을 어디에 두어야 할 것인가에 대한 고민이 생겼다. 지금 당장은 논리를 구현하는 데에 초점을 맞출 것이지만, 잘 모르겠다. 

 긴 시간은 아니었지만 하루 중 많은 시간을 투자한 프로젝트였던 만큼, 느끼고 생각하는 바가 많았던 모양이다. 이렇게 성찰할 수 있는 여력이 있는 것도 오전 수업마다 있는 멘탈케어식 진행 덕분이라고 생각한다. 성장하는 게 느껴지기만 하면 된다는 말이 어쨌든 내가 해냄, 이라는 마인드셋을 장착하게된 계기가 됐다. 부디 이 마음은 그대로, 고민과 좌절은 지금보다 덜한 6개월 후가 되어 있길 바란다.
