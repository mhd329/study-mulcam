with open('fruits.txt', 'r', encoding= 'utf-8') as f :
    fruit = f.readlines()

    cnt = 0
    for i in fruit :
        cnt += 1

    print(cnt)