with open ('./data/fruits.txt', 'r', encoding='utf-8') as f:
    my_dict = {}
    for i in f:
        i = i.strip()
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] = my_dict[i] + 1
    with open('03.txt', 'w', encoding='utf-8') as w:
        for i in my_dict:
            w.write(f'{i} {my_dict[i]}\n')