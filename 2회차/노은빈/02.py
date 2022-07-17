with open('data/fruits.txt','r',encoding='utf-8')as f:
    text=f.read()
    names = text.split('\n')

    lst=[]
    cnt=0
    for n in names:
        if n.endswith('berry'):
            lst.append(n)
    lst=list(set(lst))       
    for n in lst:     
        cnt += 1
            
    print(cnt)