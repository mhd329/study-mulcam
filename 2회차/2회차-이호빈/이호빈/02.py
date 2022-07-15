with open('2회차/2회차-이호빈/이호빈/data/fruits.txt', 'r', encoding= 'utf-8') as f:
    text = f.readlines()
    cnt = 0
    names = set(text)
    n = ""
    for name in names:
        if 'berry' in name[1:]:
            n += name
            cnt += 1
    
    print(cnt)
    print(n)