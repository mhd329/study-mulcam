cnt = 0
with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().split('\n')
    for i in text:
        cnt += 1
    print(text)
    print(cnt)