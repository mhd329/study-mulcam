with open('./data/fruits.txt', 'r', encoding='utf-8')as f:
    lines = f.readline()
    cnt = 0
    for line in f:
        if lines == ' ':
            break
        cnt += 1
    with open('01.txt', 'w', encoding='utf-8')as f1:
        f1.write(str(cnt+1))