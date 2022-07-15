with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = set(text.split('\n'))
    cnt = 0
    be = []
    for i in fruits:
        if i.endswith('berry'):
            cnt += 1
            be.append(i)
    result = '\n'.join(map(str,be))
    # print(cnt)
    # print(result)
    

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{str(cnt)}\n')
    f.write(result)