with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')
    cnt = 0
    for fruit in fruits:
        cnt += 1
    print(cnt)