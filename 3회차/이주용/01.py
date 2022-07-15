with open("data/fruits.txt", 'r', encoding='utf-8') as f:
    fruit = list(f.read().split('\n'))
print(len(fruit))
    
    