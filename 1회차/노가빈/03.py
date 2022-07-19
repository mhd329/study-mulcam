import pandas as pd
f = open('./data/fruits.txt','r')
data = f.read().splitlines()
# print(len(data))

fruitsData = {}
for i in data :
    fruitsData[i] = 0

for i in data :
    fruitsData[i] = fruitsData[i] +1
     
for i in fruitsData :
    print("%s %d"%(i,fruitsData[i]))

with open("03.txt", "w") as file:
    for i in fruitsData :
        file.write("%s %d"%(i,fruitsData[i])+'\n')