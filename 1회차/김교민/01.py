# 텍스트 데이터 입력

with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    cnt=0
    while True:
        if f.readline()=='':
            break
        cnt+=1
        a=str(cnt)

with open('01.txt', 'w', encoding = 'utf-8') as f:
    f.write(a)