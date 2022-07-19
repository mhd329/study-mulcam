with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    temp = []

    for i in f.readlines():
        temp.append(i.rstrip("\n"))
    for j in temp:    
        cnt = temp.count(j)
        print(j,cnt)

    







