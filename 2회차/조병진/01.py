# 텍스트 데이터 입력
# 과일 데이터를 활용하여 총 과일의 갯수를 기록하기

import csv

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()

a = text.split('\n')

print(len(a))
