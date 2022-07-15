with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.split('\n')
    fruit = {}

    for line in lines:
        if not line in fruit:
            fruit[line] = 1
        else:
            fruit[line] += 1

    for k, v in fruit.items():
        print(k, v)
