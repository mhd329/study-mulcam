with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruit = text.split('\n')

    fruits = list(fruit)
    fruitDict = {}

    for i in fruits:
        fruitDict[i] = 0
    for i in fruits:
        fruitDict[i] += 1

    with open('03.txt', 'w', encoding='utf-8') as f:
        for k, v in fruitDict.items():
            f.write(f'{k} {v}\n')