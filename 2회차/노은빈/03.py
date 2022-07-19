with open('data/fruits.txt','r',encoding='utf-8')as f:
    text=f.read()
    names = text.split('\n')
    lst ={}
    for i in names:
        if not i in lst:
            lst[i] = 1
        else:
            lst[i] += 1
    for key,value in lst.items():
        c=str(value)
        print(key,value)        
    #어제의 8번 문제