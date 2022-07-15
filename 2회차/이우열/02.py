with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.split('\n')
    cnt = 0
    berry = []

    for line in lines:
        if line.endswith('berry'):
            if not line in berry:
                berry.append(line)
                cnt += 1

    print(cnt)

    for line in berry:
        print(line)
