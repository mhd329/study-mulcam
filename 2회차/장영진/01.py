with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = list(text.split('\n'))
    cnt = 0

    for i in names:
        # print(i)
        cnt += 1

print(cnt)