with open('data/fruits.txt', 'r',encoding='utf-8') as f:
    cnt = 0
    while True:
        text01 = f.readline()
        cnt+=1
        if text01 == 'berryfake':
            break

    d= open('01.txt','w',encoding='utf-8')
    d.write(str(cnt))