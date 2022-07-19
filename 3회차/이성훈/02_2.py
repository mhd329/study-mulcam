with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    cnt = 0
    lines = f.readlines()
    print(lines, type(lines))

print(cnt)