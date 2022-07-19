import pprint

cnt_fruits = {}

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read() 
    line = text.split('\n')

    for fruits in line:
        if fruits in cnt_fruits:
            cnt_fruits[fruits] += 1
        else:
            cnt_fruits[fruits] = 1

pprint.pprint(cnt_fruits)

with open('03.txt', 'w', encoding='utf-8') as f:
    for k, v in cnt_fruits.items():
        f.write(f'{k} {v}\n')