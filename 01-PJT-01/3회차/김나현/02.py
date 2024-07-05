with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    str = f.read()
    res = []
    fruit_list = str.split('\n')
    for fruit in fruit_list:
        if (fruit[len(fruit) - len('berry'):len(fruit)] == 'berry'):
            findcheck = fruit in res
            if (findcheck == False):    #   비어있는 경우
                res.append(fruit)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(res)}\n')
    for fruit in res:
        f.write(f'{fruit}\n')