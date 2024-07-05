with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names =text.split()
    cnt = 0
    for i in names:
        if 'berry' in names:
            cnt += 1
print(cnt)



