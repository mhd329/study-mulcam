with open('data/fruits.txt','r', encoding = 'utf -8') as f:
   text = f.read()
   names = text.split('\n')
   do=[]
   po =list(set(names))
   cnt = -1
   for b in po:
    if "berry" in b:
        do.append(b)
        cnt +=1

print(cnt)
print(do)