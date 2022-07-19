with open('1회차/박치우/data/fruits.txt','r',encoding='utf-8') as f:
    text = f.read()
    text = text.split('\n')
dic = {}
for i in text:
    if i not in dic :
        dic[i] = 1
    else:
        dic[i] += 1
for i in dic:
    print(i, dic[i])


