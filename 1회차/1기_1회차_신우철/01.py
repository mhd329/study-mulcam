with open('data/fruits.txt','r',encoding='utf-8') as f:
    count = 0
    while True:
        if f.readline()=='':
            break
        count += 1
    print(count)
        