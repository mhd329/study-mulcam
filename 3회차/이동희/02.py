count = 0
fruit_list = []
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    for fruit in f:
        if fruit.endswith('berry\n'):
            if fruit not in fruit_list:
                count += 1
                fruit_list.append(fruit)
            else:
                continue
    f.close()
    
with open('02.txt', 'w', encoding='utf-8') as txt_02:
    txt_02.write(f'{str(count)}\n')
    for berry in fruit_list:
        txt_02.write(berry)
    txt_02.close()