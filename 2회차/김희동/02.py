with open('data/fruits.txt', 'r', encoding='utf-8') as f:

    text = f.read()
    fruits = text.split('\n')
    cnt = 0
    list=[]
    
    for fruit in fruits:
        if fruit.endswith('berry'):
            if fruit not in list:
                cnt += 1
                list.append(fruit)

with open('02.txt', 'w', encoding='utf-8') as ff:
    ff.write(f'{cnt}\n')
    for i in list:
        ff.write(f'{i}\n')