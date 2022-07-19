b = 0
with open('./data/fruits.txt', 'r', encoding='UTF8') as f:
    t = f.readlines()
    for i in t:
        if 'berry' in i:
            b += 1
print(b)