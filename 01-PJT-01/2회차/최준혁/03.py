from select import kevent
import sys

with open(r"/Users/mac/Desktop/KDT_PROJ/01-PJT-01/2회차/최준혁/data/fruits.txt", 'r', encoding='utf-8') as f:
    text = f.read()
    fruit = text.split("\n")
    dict_fruit = {}

    for char in fruit:
        if char in dict_fruit:
            dict_fruit[char] += 1
        else:
            dict_fruit[char] = 1

    for v, k in dict_fruit.items():
        print(v, k, end='')

sys.stdout = open('03.txt', 'w')
for k, v in dict_fruit.items():
    print(k, v) 
sys.stdout.close()