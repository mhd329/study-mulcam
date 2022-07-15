with open('1회차/박치우/data/fruits.txt','r',encoding = 'utf-8') as f:
    text = f.read()
a = 'berry'
s = set()
text = text.split('\n')
for i in text:
    if i[0] != a and a in i:
        s.add(i)
print(len(s))
s = list(s)
for i in range(len(s)):
    print(s[i])
   