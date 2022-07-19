

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f. read()
    count = 1
    for i in text:
        if i == '\n':
            count += 1
            print(count)