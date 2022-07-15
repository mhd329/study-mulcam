with open ('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    frt = text.split('\n')
    print(len(frt))
    n = len(frt)

with open ('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(n))