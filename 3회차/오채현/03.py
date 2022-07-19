with open ('./data/fruits.txt', 'r', encoding='utf-8') as f:
    
    cnt_frt = {}
    i = 0
    for line in f:
        if not line in cnt_frt:
            cnt_frt[line] = 1
        else:
            cnt_frt[line] = cnt_frt[line] + 1
    

with open('03.txt', 'w', encoding='utf-8') as f:
    for key in cnt_frt:
        f.write(f'{key} {cnt_frt[key]}\n')
    