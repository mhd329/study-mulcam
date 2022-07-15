a = list()
new_list = list()
cnt = 0
with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().split('\n')

    for i in text:
        if i.endswith('berry'):
            a.append(i) 

    for i in a:
        if i not in new_list:
            new_list.append(i)

    for i in new_list:
        cnt += 1
    print(cnt, *new_list, sep='\n')