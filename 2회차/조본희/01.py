with open('data/fruits.txt', 'r', encoding='utf-8') as r:
    text = r.read()
    fruits = text.split('\n')
    print(len(fruits))
