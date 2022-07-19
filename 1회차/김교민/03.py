with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    a={}
    for i in f:
        l=str.split(i, '\n')
        for b in l:
            if b in a:
                a[b]+=1
            else:
                a[b]=1
with open('03.txt', 'w', encoding = 'utf-8') as f:
    for k, v in a.items():
        f.write(f'{k}, {v}\n')