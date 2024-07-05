with open('./data/fruits.txt', 'r', encoding='utf-8')as f:
    cnt = 0
    result=[]
    fr = f.readlines()
    with open('02.txt', 'w', encoding='utf-8')as f1:
        for line in fr:
            if line not in result:
                result.append(line)
                if line.endswith('berry\n'):
                    cnt += 1
                    f1.write(str(line))
        f1.write(str(cnt))