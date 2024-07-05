#lines[-5:]
lines = " "
Outputlist = []
cnt = 0
with open('C:/Users/rkaeh/Desktop/01-PJT-01/2회차/감동재/data/fruits.txt','r',encoding = 'utf-8') as f:
    while lines != "":
        lines = f.readline()
        if lines[-6:]=='berry\n':
            cnt+=1
            Outputlist.append(lines)

print(len(Outputlist))

with open('C:/Users/rkaeh/Desktop/01-PJT-01/2회차/감동재/02.txt','w',encoding = 'utf-8') as f:
     f.write(str(len(Outputlist))+"\n")
     for o in Outputlist:
        f.write(o)




print(cnt)
