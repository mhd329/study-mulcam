berries = set()

with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read() # 전체 읽기 및 string type
    line = text.split('\n')

    for fruit in line:
        if fruit.endswith('berry'):
            berries.add(fruit)

print(len(berries))
        
with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(berries)}\n')
    for i in range(len(berries)):
        f.write(f'{berries.pop()}\n')