# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.
 # 과일 데이터를 for문을 통해 순환시키고 if문으로  딕셔너리 키와 값 쌍을 만든다.

 # 이후 만든 키 값쌍을 이름과 등장횟수로 만든 후 03.txt에 보내기 



with open ('data/fruits.txt','r',encoding='utf8') as f:
    fruits = f.read() 


lsfru = fruits.split('\n')  # *문제점1. 리스트로 만들지 않아서 알파벳별로 분류가 되었다. split을 통해 리스트를 만들어주자


fdict = {} #딕셔너리로 과일과 카운트숫자 키 값을 for문과 if문으로 배정

for fru in lsfru : #리스트에있는 과일들을 fru로 하나씩 순환
    if fru in fdict: 
        fdict[fru] += 1# 순환중에 fdict (딕셔너리)에 과일이 있다면 '과일명에 1로 더해주고 저장
    elif not fru in fdict:# 순환중에 fdict (딕셔너리)에 과일이 없다면 '과일명 : 1'로 저장
        fdict[fru] = 1

# print (fdict,type(fdict))

with open ('03.txt','w',encoding='utf8') as se: #*encoding이 잘적혔는지 확인 파란글씨라 틀렸는지 안나옴)
    for k,y in fdict.items():
        
        se.write(f'{k} {y}\n') # *키 값쌍을 괄호지우고 ,지우고 sep사용해서 공백넣으려고 1시간넘게 고민.. 단순하게 생각하자 그냥 띄어쓰기만 하면되는걸 ㅠㅠ

print () 
# kk= k,y

# print (kk)
