with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    a={}
    for i in f:
        l=i.split('\n')
        for b in l:
            if b in a:
                a[l]+=1
            else:
                a[1]==1