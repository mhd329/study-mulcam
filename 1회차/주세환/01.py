
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    name = text.split('\n')
    cnt = 0

    for i in name:
        cnt += 1
    with open('01.txt', 'w', encoding='utf-8') as f:
        f.write(str(cnt))


