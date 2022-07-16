import pandas as pd
f = open('./data/fruits.txt','r')
data = f.read().splitlines()
print(len(data))

with open("01.txt", "w") as file:
    file.write(str(len(data)))