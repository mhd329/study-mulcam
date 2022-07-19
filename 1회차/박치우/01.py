with open('1회차/박치우/data/fruits.txt','r',encoding = 'utf-8') as f:
    text = f.read()
    text = text.split('\n')
print(len(text))