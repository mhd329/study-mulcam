with open('2회차/이상백/data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read()
    print(fruits.count('\n')+1)