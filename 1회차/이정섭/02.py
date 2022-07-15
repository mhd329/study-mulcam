with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.readlines()
    cnt = 0
    for fruit in fruits:
        print(fruit)
        if fruit.endswith('berry\n'):
            cnt = cnt + 1
    print(cnt)