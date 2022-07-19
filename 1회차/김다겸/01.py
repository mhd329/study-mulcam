with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()

    fruits = text.split("\n")
    
    print(len(fruits))

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(len(fruits)))