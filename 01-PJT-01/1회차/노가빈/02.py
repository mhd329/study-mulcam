import pandas as pd
f = open('./data/fruits.txt','r')
data = f.read().splitlines()
data = list(set(data))
fList=[]
c = 0

for i in data :
        if i.endswith('berry') :
            fList.append(i)
            c = c + 1

with open("02.txt", "w") as file:
    file.write(str(c)+'\n')
    for i in data :
        if i.endswith('berry') :
            file.write(i+"\n")