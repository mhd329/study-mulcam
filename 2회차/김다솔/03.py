with open('data/fruits.txt', 'r', encoding='utf-8') as f:
        
    dict = {}
    
    for fruit in f:
        if fruit not in dict:
            dict[fruit] = 1
        else:
            dict[fruit] = dict[fruit] + 1
            
with open('03.txt', 'w', encoding='utf-8') as f: 
    for k, v in dict.items():
        f.write(f'{k} {v}\n')