with open('data/fruits.txt','r',encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    y = list(names)
    dic = {}
    for i in y:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
import sys
sys.stdout = open('03.txt','w',encoding='utf-8')
for key in dic.keys():
        print(key,'', dic[key]) 