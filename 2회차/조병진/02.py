# 텍스트 데이터 활용
# 과일 데이터를 활용하여 berry로 끝나는 과일의 갯수와 목록을 기록하기

import csv

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()

a = text.split('\n')
berry_list = []

for i in a:
    if i[-5:] == 'berry':
        n = i.split('\n')
        berry_list = n + berry_list

n = set(berry_list)

print(len(n))
print(list(n))
