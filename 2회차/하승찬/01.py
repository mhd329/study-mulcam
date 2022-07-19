
#데이터 파일을 furit.txt 읽기전용으로 뽑고 나서 바로 카운트를 하게 되면 글자수가 다 카운트됨
#이걸 방지하기 위해 split를 사용해 리스트로 묶어주고 리스트를 for함수를통해 횟수마다 1씩 카운트한다.
#카운트 한 숫자를 txt파일을 만들어 갯수를 저장해보자
with open('data/fruits.txt','r',encoding='utf-8') as f: # 연 파일의 이름 지정 as :f f는 파일명
   fruit = f.read()
a = (fruit.split('\n')) # 과일들의 리스트

count = 0
for fru in a:   #이렇게 카운트하게된다면  과일들의 숫자를 카운트변수에 할당 가능하다.
        count+= 1
        
with open('01.txt','w',encoding='utf-8') as b: # 01.txt파일을 만든다 b라는 이름으로 저장
    b.write(str(count))                             # 위의 카운트한 숫자를 b의 txt파일에 쓴다 (with함수로 자동저장)
                                               # utf-8을 잘 기억하자 LookupError: unknown encoding: udf-8
                                               # wirte는 문자로만 저정된다 str로 바꾸기