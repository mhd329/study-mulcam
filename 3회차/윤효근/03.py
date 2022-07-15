from collections import Counter

f = open("data\\fruits.txt",'r')
w=open("03.txt",'w')
tmp = f.readlines()
cnt = Counter(tmp)
for i in cnt.items():
    w.write(f'{i[0]}{i[1]}'+'\n')