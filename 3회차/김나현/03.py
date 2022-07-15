with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    str = f.read()
    res = {}
    fruit_list = str.split('\n')
    for fruit in fruit_list:
        findcheck = fruit in res
        if (findcheck == False):
            res[fruit] = 1
        else:
            res[fruit] += 1
with open('03.txt', 'w', encoding='utf-8') as f:
    for i in res:
        f.write(f'{i} {res[i]}\n')