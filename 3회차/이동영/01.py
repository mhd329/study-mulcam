with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    count = 0
    for i in lines:
        count += 1
print(count)
