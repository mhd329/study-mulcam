with open('data/fruits.txt','r',encoding='utf-8')as f:
    text = f.readlines()
    
    cnt=0
    for n in text:
     if n in text :
        cnt += 1
    print(cnt)

#read 활용
with open('data/fruits.txt','r',encoding='utf-8')as f:
    text = f.read()
    names = text.split('\n')
    
    cnt=0
    for n in names:
     if n in names:
        cnt += 1
    print(cnt)