with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
    count = 0
    new_list = []
    for list in l:
        if list.endswith('berry\n'): # 여기까지 맞음
            if list not in new_list:
                count += 1
                new_list.append(list)
                result = str(count)
                str_list = ''.join(new_list)

with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(result)
    f.write('\n')
    f.write(str_list)