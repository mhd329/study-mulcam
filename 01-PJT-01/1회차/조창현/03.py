f = open('data/03.txt', 'w')
f.close()
with open('data/fruits.txt', 'r', encoding='utf-8')as f:
    fruits = f.read().split('\n')
    fruit_l = []
    fruit_n = []
    for fruit in fruits:
        if fruit not in fruit_l:
            fruit_l.append(fruit)
    print(fruit_l)
    for i in fruit_l:
        cnt = 0
        for j in fruits:
            if i == j:
                cnt += 1
        fruit_n.append(f'{i} {cnt}')
    print(fruit_n)

with open('data/03.txt', 'w', encoding='utf-8')as f:
    for fruit in fruit_n:
        f.write(f'{fruit}\n')