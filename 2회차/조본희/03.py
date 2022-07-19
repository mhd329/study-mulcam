with open('data/fruits.txt', 'r', encoding='utf-8') as r:
    text = r.read()
    fruit = text.split('\n')

#Dictionary 생성해서 key, value 저장
fruits = list(fruit)
fruitDict = {}

for i in fruits:
    fruitDict[i] = 0
for i in fruits:
    fruitDict[i] += 1

#txt파일 만들어서 저장
with open('03.txt', 'w', encoding='utf-8') as w:
    for k, v in fruitDict.items():
        w.write(f'{k} {v}\n')
