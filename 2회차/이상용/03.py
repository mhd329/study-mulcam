# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.

# 0714 8번문제와 유사, 딕셔너리 생성 후

frt = {}
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        frt[line] = frt.get(line, 0) + 1

with open('03.txt', 'w', encoding='utf-8') as ff:
    for i in frt:
        tmp = i.strip('\n') + ' ' + str(frt[i]) + '\n'
        ff.write(tmp)