with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.readlines()
    names = fruits
    cnt = 0
    for fruit in names:
        cnt += 1
    print(cnt)

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt))