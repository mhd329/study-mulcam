f = open('data/02.txt', 'w')
f.close
with open('data/fruits.txt', 'r', encoding='utf-8')as f:
    fruits = f.read().split('\n')
    #print(fruits, type(fruits))
    cnt = 0
    fruit_l = []
    for fruit in fruits:
        if (fruit.endswith('berry')):
            if(fruit not in fruit_l):
                fruit_l.append(fruit)
    print(len(fruit_l))
    for fruit in fruit_l:
        print(fruit)

with open('data/02.txt', 'w', encoding='utf-8')as f:
    f.write(f'{len(fruit_l)}\n')
    for fruit in fruit_l:
        f.write(f'{fruit}\n')