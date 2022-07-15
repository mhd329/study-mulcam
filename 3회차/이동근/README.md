# 프로젝트 01 - 파이썬 기반 데이터 활용

<br/>

## 배운 것
<hr/>
<br/>

### 1. with ~

    with {expression} as {variable}:
        Code Block

<br/>

**설명**

- 자원을 획득/사용/반납 할 때 주로 사용된다. 
 
- 예를 들면 파일 open, DB Session 사용할 경우 다른 프로세스를 위해 반납 해야한다.

- 해당 statement 는 Race Condition 을 예방하기 위해 파이썬에서 제공하는 Critical Section 으로 보인다.

- 내부적으로 어떻게 동작하는지는 모르겠으나 결과적으로 lock 을 이용하는거 같은데 나중에 살펴봐야할 것 같다.

<br/>

**ex) 아래는 예시이다.**

1.  with 적용 안한 전통적인 코드
    ```
    f = open('myFile.txt', 'w', encoding='utf8')
    f.write("test")
    f.close()
    ```

2.  with 적용한 코드
    ```
    with open('mytextfile.txt', 'r', encoding='utf8') as f:
    f.wirte("test")
    ```

<br/>
<hr/>
<br/>

### **2. files.readlines() / files.readlines()**

<br/>

    file.readlines()
    file.writelines()

**설명**

- 해당 file 객체를 모든 줄을 읽/쓴(는)다.

- 반환값은 readlines() 의 경우, 각 줄이 리스트의 content로 들어가며 각 content 의 자료형은 str 이다.
-  writelines 메소드의 인자로 list 를 넣어보았으나 동작하지 않는다. 아마 stream 이라는 타입의 객체만 받을 것이라고 생각한다.
- 공식 문서에는 "Read and return a list of lines from the stream." 으로 서술되어 있다. 이 부분은 추후에 다시 시도 해봐야할 것 같다.

<br/>
<hr/>
<br/>

### **3. 딕셔너리 컴프리헨션 내가 놓친 부분**

<br/>

    d = {i:num[i] for i in iterable}

<br/>

**설명**
- 딕셔너리므로 "키:값" 의 형태를 서술 해야하는데 그러지 않았다.
- ```{i for i in iterable}``` 형태로 작성했기 때문에 아까운 시간만 낭비했다.


<br/>
<hr/>
<br/>

### **4. sorted() 내장 함수**

<br/>

    sorted(iterable, /, *, key=None, reverse=False)

**설명**
- iterable 에 속한 정렬된 item 들이 있는 "새로운" list 를 반환한다.
- reverse 가 False : 오름, True : 내림차순이다.
- key 는 iterable 에 각 요소들과 비교하는 키를 얻는데 쓰는 하나의 인자를 받는 함수를 지정한다. 

- 원문을 직역하니 어려워지는데 쉽게 말하면 해당 함수를 이용해서 구체적으로 "무엇을" 기준으로 정렬할지를 의미한다.

<br/>
<hr/>
<br/>

## 후기

- 점점 해당 코스에서 어떻게 진행을 할지 감이 잡힌다. 
- 현재 파일 입출력까지 진행됐는데 Django 로 넘어갈 때, URL 을 가지고 JSON 같은 형식의 데이터를 적절하게 가공하여 DB 에 적용 하기 위한 일종의 기초 작업 공사같다.

- 나도 파이썬을 잘 모르지만 with statement 나 json, pprint 모듈은 처음 써봤기 때문에 새로운 것을 배운 좋은 시간이였다.

<br/>

## 참조
<hr/>
<br/>

[1. Python with절 문법의 이해](https://projooni.tistory.com/entry/Python-with%EC%A0%88-%EB%AC%B8%EB%B2%95%EC%9D%98-%EC%9D%B4%ED%95%B4)

[2. io.IOBase.readlines, io.IOBase.writelines](https://docs.python.org/3/library/io.html?highlight=readlines#io.IOBase.readlines)

[3. 파이썬 딕셔너리 value 로 값 정렬 방법](https://korbillgates.tistory.com/171)

<br/>
<hr/>
<br/>