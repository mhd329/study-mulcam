
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split()
    berries ={}

    for i in names:
        if i in berries:
            berries[i] += 1
        else:
            berries[i] = 1

with open('03.txt', 'w', encoding='utf-8') as f2:
    for k, v in berries.items():
        f2.write(k + ' ')
        f2.write(str(v) + '\n')
