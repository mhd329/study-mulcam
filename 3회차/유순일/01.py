with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.readlines()
    fruit = list(fruits)
    number = len(fruit)
    print(number)
    
with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(number))