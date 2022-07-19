with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    a={}
    cnt=0
    f=set(f)
    for i in f:
        l = str.split(i, '\n')
        for j in l:
                if j.endswith("berry"):
                    if j in a:
                        a[j]+=1
                    else:
                        a[j]=1
                        cnt+=1
with open('02.txt', 'w', encoding = 'utf-8') as f:
    d=str(cnt)
    f.write(f'{d}')
    for i in a:
        f.write(f'\n{i}')