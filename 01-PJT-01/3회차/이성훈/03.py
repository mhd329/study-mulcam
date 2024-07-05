# 과일 데이터 fruits.txt를 활용하여 
# 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.


result = {}

with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    for i in f:
        i = i.rstrip('\n')
        
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1

for key in result:
    print(key, result[key])