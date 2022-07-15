with open('data/fruits.txt', 'r', encoding='utf-8')as f:
    fruit = f.read()
    fruits = fruit.split('\n')
    data = {}

    for i in fruits :
        if i in data :
            data[i]+=1
        else :
            data[i]=1
with open('03.txt', 'w', encoding='utf-8')as f:
    for i in data :
        f.write(f'{i} {data[i]}\n')