with open('data/fruits.txt', 'r', encoding='utf-8') as r:
    text = r.read()
    fruits = text.split('\n')

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(len(fruits)))