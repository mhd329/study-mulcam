# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.


with open('data/fruits.txt', 'r', encoding='utf-8') as f:

    text = f.read()
    result = text.split()
    

    result1 = {}
for char in result:
    if not char in result1:
        result1[char] = 1
    else:
        result1[char] = result1[char] + 1


result1 = {}
for char in result:
    result1[char] = result1.get(char, 0) +1

for key in result1:
    print(key, result1[key])