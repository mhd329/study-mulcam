frt = {}
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        frt[line] = frt.get(line, 0) + 1

with open('03.01.txt', 'w', encoding='utf-8') as ff:
    for i in frt:
        tmp = i.strip('\n') + ' ' + str(frt[i]) + '\n'
        ff.write(tmp)