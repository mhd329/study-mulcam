with open('2회차/백솔비/data/fruits.txt', 'r', encoding='utf-8') as f:

    text = f.read()
    name = text.split()

    d = {}
    for i in name:
        d[i] = d.get(i, 0)+1

for key, value in d.items():
    print(key, value)

with open('2회차/백솔비/03.txt', 'w', encoding='utf-8') as f:
    for key, value in d.items():
        f.write(f'{key} {value}\n')
