with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    cnt = 0
    li =[]
    for line in f:
        if line == 'berry':
            cnt += 1
            li.append(line)
        print(li)


# with open('02.txt', 'w', encoding='utf-8') as f:
