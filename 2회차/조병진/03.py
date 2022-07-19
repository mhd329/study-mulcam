# 텍스트 데이터 활용 - 등장 횟수
# 과일 데이터를 활용하여 과일의 이름과 등장 횟수를 기록하기

import csv

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()

a = text.split('\n')
n = {}

for i in a:
    try:
        n[i] += 1
    except:
        n[i] = 1

for x, y in n.items():
    print(x, y)
