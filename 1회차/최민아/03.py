f = open('data/fruits.txt', 'r', encoding='utf-8')
fruit = {}
for name in f:
    name = name.strip()
    if name in fruit:
        fruit[name] += 1
    else:
        fruit[name] = 1
f.close()

with open('03.txt', 'w', encoding='utf-8') as f:
    for key, value in fruit.items():
        f.write(f'{key} {value}\n')
    f.close()

