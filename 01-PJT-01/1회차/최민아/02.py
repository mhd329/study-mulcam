f = open('data/fruits.txt', 'r', encoding='utf-8')
cnt = 0
berry = []
for name in f:
    if name[-6:-1] == 'berry':
        if name not in berry:
            cnt += 1
            berry.append(name)
f.close()

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{cnt}\n')
    for b in berry:
        f.write(b)
    