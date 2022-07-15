with open('2회차/2회차-이호빈/이호빈/data/fruits.txt', 'r', encoding= 'utf-8') as f:
    names = f.readlines()
    cnt = 0
    for name in names:
        cnt += 1
    
    print(cnt)
