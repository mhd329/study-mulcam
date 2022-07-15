
with open('data/fruits.txt', 'r', encoding= 'utf-8') as f:
    text = f.read()
    name = text.split('\n')
    result = {}

    for i in name:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
        
with open('03.txt', 'w', encoding='utf-8') as f:
    for k, v in result.items():
        f.write(f'{k} {v}\n')
