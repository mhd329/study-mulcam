# 과일 데이터 fruits.txt를 활용하여 총 과일의 갯수를 01.txt  에 기록하시오.

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')

print(len(fruits))

with open('01.txt', 'w', encoding='utf-8') as a:
    a.write(f'{len(fruits)}')


