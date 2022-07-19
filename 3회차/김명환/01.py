
with open('data\\fruits.txt' , 'r',encoding='utf-8') as f:
    cnt = 0
    while True:
        if f.readline() == '':
            break
        cnt+=1
    print(cnt)    

with open('01.txt', 'w',encoding='utf-8') as f:
     f.write(f'{cnt}')