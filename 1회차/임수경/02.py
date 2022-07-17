with open(r'C:\Users\LGE\Desktop\01-PJT-01\1회차\임수경\data\fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    my_list = text.split('\n')
    berries = {}
    cnt = 0
    
    for i in my_list:
        if i.endswith('berry'):

            if i in berries:
                berries[i] += 1
            else:
                berries[i] = 1
                cnt += 1

with open('02.txt', 'w', encoding='utf-8') as f2:
    f2.write(str(cnt) + '\n')
    for i in berries:
        f2.write(i + '\n')