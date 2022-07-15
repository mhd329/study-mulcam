with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split()
    cnt = 0

    for name in names:
        if name.endswith('berry'):
            berry = (se)
            cnt += 1
    
    print(cnt)