with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.split('\n')
    cnt = 0

    for line in lines:
        cnt += 1

    print(cnt)
