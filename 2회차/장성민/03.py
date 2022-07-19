import pprint

with open('data/fruits.txt', 'r', encoding = 'UTF-8') as f:
    names = f.read().split()

dic = {}

for name in names:
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

keyList = dic.keys()
valueList = dic.values()


pprint.pprint()


