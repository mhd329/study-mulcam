with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    str = f.read()
    fruit_list = str.split('\n')
    cnt = 0
    for fruit in fruit_list:
        cnt += 1

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(f'{cnt}')