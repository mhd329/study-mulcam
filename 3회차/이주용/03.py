with open("data/fruits.txt", 'r', encoding='utf-8') as f:
    fruit = list(f.read().split('\n'))
    
fruit_dict = {}
for i in fruit:
    if i not in fruit_dict:
        fruit_dict[i] = 1
    else:
        fruit_dict[i] += 1
        
for i in fruit_dict:
    print(i, fruit_dict[i])