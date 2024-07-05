with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    list = f.read()
    fruits = list.split('\n')
    berries = {}
    cnt = 0

    for berry in fruits:
        if berry.endswith('berry'):
            if berry in berries:
                berries[berry] += 1
            else:
                berries[berry] = 1
                cnt += 1

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt) + '\n')
    for berry in berries:
        f.write(berry+'\n')