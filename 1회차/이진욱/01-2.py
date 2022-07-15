with open('data/fruits.txt', 'r',encoding='utf-8') as f:
    cnt = 0
    while True:
        text01 = f.readline()
        cnt+=1
        if text01 == '':
            break
    print(cnt-1)

    d= open('01-2.txt','w',encoding='utf-8')
    d.write(str(cnt-1))