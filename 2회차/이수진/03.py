with open("2회차/이수진/data/fruits.txt", 'r',encoding='utf=8') as f:
    with open("2회차/이수진/data/03.txt", 'w',encoding='utf=8') as f2:
        flist=f.readlines()
        fdic={}
        for i in flist:
            
            if i in fdic :
                fdic[i.strip('\n')]+=1
            else:
                fdic[i.strip('\n')]=1

        for name,cnt in fdic.items():
            f2.write(f'{name} {cnt}\n')
        

