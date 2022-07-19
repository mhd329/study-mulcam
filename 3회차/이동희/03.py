fruit_dict = {}
    
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for fruit in f:
        if '\n' in fruit:
            fruit = fruit.strip('\n')
            if fruit not in fruit_dict.keys():
                fruit_dict[fruit] = 1
            elif fruit in fruit_dict.keys():
                fruit_dict[fruit] += 1
        else:
            if fruit not in fruit_dict.keys():
                fruit_dict[fruit] = 1
            elif fruit in fruit_dict.keys():
                fruit_dict[fruit] += 1
    f.close()
    
with open('03.txt', 'w', encoding='utf-8') as txt_03:
    for key, value in fruit_dict.items():
        txt_03.write(f'{key} {value}\n')
    txt_03.close()