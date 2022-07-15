# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.


with open ('data/fruits.txt','r',encoding='utf8') as f:
    fruits = f.read() 


for fru in fruits :
