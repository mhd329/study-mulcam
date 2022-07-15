with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruit = f.read()
    li = []
    fruit.append('\n')
    print(fruit(type(fruit)))