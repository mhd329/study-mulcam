with open("2회차/이수진/data/fruits.txt", 'r',encoding='utf=8') as f:
    with open("2회차/이수진/data/02.txt", 'w',encoding='utf=8') as f2:
        fset=set(f.readlines())
        cnt=0        
        for i in fset:
            if 'berry' in i.lstrip('berry'):
                cnt+=1
        print(str(cnt))
        f2.write(str(cnt))
        f2.write('\n')
        for i in fset:
            if 'berry' in i.lstrip('berry'):
                f2.write(i)
                print(i)