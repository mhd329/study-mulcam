# 과일 데이터 fruits.txt를 활용하여 총 과일의 갯수를 01.txt에 기록하시오.

with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    fruits = f.read()
    fruits_list = fruits.split('\n')
    
    print(len(fruits_list))

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(len(fruits_list)))