# - 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read() # 읽은 fruits는 string 타입임.
    print(fruits)
    fruits_list = fruits.split('\n') # 줄바꿈을 뛰어쓰기로 인식한 것 같음. string.split()는 list 타입임
    
    number=0
    for num in fruits_list:
        number += 1    
    print(number)
with open('01.txt', 'w', encoding = 'utf-8') as f:
    f.write('394')