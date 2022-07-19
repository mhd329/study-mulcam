with open('data/fruits.txt','r',encoding='utf-8') as f:
    text = f.readlines()   
    names = text.split()
    cnt = 0
    for name in names:
        if name.startswith('berry'):    
            cnt += 1
    print(cnt)
