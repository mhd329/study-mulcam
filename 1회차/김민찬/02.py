with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')

    list = []
    for fruit in fruits:
        if fruit.endswith('berry'):
            list.append(fruit)

    result = []
    for i in list:
        if i not in result:
            result.append(i)

    with open('02.txt', 'w', encoding='utf-8') as f:
        f.write(f'{len(result)}\n')
        for i in result:
            f.write(f'{i}\n')