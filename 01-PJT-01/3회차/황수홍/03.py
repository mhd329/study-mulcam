with open('./data/fruits.txt', 'r', encoding='utf-8')as f:
    dic = {}
    fr = f.readlines()
    for i in fr:
        if i in dic:
            dic[i] += 1
        else :
            dic[i] = 1
    with open('03.txt', 'w', encoding='utf-8')as f1:
        for i in dic:
            f1.write(i)
            f1.write(str(dic[i])+'\n')