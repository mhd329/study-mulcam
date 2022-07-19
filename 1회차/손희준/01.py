with open('data/fruits.txt','r',encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    y = list(names)
    cnt = 0
    for i in y:
        if i.startswith(""):
            cnt += 1
import sys
sys.stdout = open('01.txt','w',encoding='utf-8') 
print(cnt)