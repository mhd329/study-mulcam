with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split("\n")
    d = dict()
    result = []

    for i in fruits:
        if i not in result:
            result.append(i)

with open('03.txt', 'w', encoding='utf-8') as f:
        for fruit in result:
            if fruit not in d:
                d[fruit] = 1
            else:
                d[fruit] = d[fruit] + 1
            d_fruit = "{}".format(d[fruit])
            print(fruit, d[fruit])
            f.write(fruit + " " + d_fruit + "\n")