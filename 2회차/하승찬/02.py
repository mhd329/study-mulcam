# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 02.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.

# 과일데이터 파일을 열고 리스트로 지정해 준 뒤 for문과 if문을 사용해서
#  뒤의 글자가 berry로 끝나는 갯수와 목록을 변수에 할당 후 02.txt파일에 저장해준다.

with open('data/fruits.txt','r',encoding='utf-8') as f: # 연 파일의 이름 지정 as :f f는 파일명
   fruit = f.read()
idx = fruit.split('\n')  #텍스트 파일의 과일들을 목록으로 정리 
fname =[]                #목록들이 베리와 일치한다면 fname의 인덱스에 더해준다
count = 0                # 베리와 일치하는 과일들의 숫자를 카운트
for fru in idx: 
    if fru.endswith('berry'): # 마지막이 berry로 끝나는지 판단 *동일한 이름의 베리가 존재해서 중첩으로 계산됨
        if not fru in fname : #  if문을 통해fru가  fanme 추가되는 과일 명단에 없다면 1카운트와 과일명단에 이름 추가
            count+= 1
            fname.append(fru)      

count_str = str(count)
# fname_str = ",".join(fname)    # *삽질 굳이 str으로 만들고 안해도 됬음 
# fname_str1 = (f'{fname_str}\n') # for문을 사용해서 목록을 꺼내서 사용하면됨
                                  # 굳이 b.write(f'fname_str1}\n')로 바로 보내려고하다 보내지지가 않아서 시간버림
                                  # 리스트는 for문을 꺼내서 하나씩 보내자 (자동 str됨)

with open('t02.txt','w',encoding='utf-8') as b: 
    b.write(f'{count_str}\n')
    for fs in fname:
        b.write(f'{fs}\n')

