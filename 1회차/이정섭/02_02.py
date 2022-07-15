with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read()
    print(fruits)
    berries = fruits.split()
    cnt = 0
    for berry in berries:
        if berry('berry'):
            cnt += 1
    print(cnt)