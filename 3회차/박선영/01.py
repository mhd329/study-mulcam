cnt = 0
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for i in f:
        cnt += 1

with open('01.txt', 'w', encoding='utf-8') as f01:
    f01.write(f'{cnt}')