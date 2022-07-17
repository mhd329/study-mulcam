with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = set(text.split('\n'))
    cnt = 0
    for i in fruits:
        if i.endswith('berry'):
            cnt += 1
            print(i)
    # print(cnt)

with open('02.txt', 'w', encoding="utf-8") as f2 : 
    f2.write(str(cnt))