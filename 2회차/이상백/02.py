with open('2회차/이상백/data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read()
    cnt = 0
    sample = fruits.split('\n')
    for i in sample:
        if i.rfind('berry') :
            cnt += 1
    print(cnt)