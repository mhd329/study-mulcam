with open('./data/fruits.txt', 'r', encoding = 'utf-8')as f:
    fruit = f.readlines()
    cnt = 0
    overlap = []
    for i in fruit:
        if i not in overlap:
            overlap.append(i)
            if i.endswith('berry\n'):
                    cnt += 1
                    print(i, end='')
    print(cnt)