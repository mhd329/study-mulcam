with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    result = {}
    for i in f:
        i = i.strip()
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

with open('03.txt', 'w', encoding='utf-8') as f:
    for key, value in result.items():
        f.write(f'{key} {value}\n')
