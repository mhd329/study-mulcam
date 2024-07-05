with open('data/fruits.txt', 'r', encoding='utf-8') as f, open('02.txt', 'w', encoding='utf-8') as f2 :
    fruit = f.readlines()
    # print(fruit, type(fruit))
    for line in fruit:
        # print(line, type(line))
        if 'berry' in line :
            # print(line)
            f2.write(line)